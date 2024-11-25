import json
from types import SimpleNamespace
import re

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = self._load_config()

    def _load_config(self):
        """Load JSON and replace placeholders recursively."""
        with open(self.file_path, 'r') as f:
            config_data = json.load(f)

        def replace_placeholders(obj, root_config):
            if isinstance(obj, dict):
                return {k: replace_placeholders(v, root_config) for k, v in obj.items()}
            elif isinstance(obj, str):
                # Replace placeholders with values from anywhere in the config
                def replacer(match):
                    key = match.group(1)
                    # Search recursively through the entire configuration
                    def find_key_value(config, target_key):
                        if isinstance(config, dict):
                            if target_key in config:
                                return str(config[target_key])
                            for value in config.values():
                                result = find_key_value(value, target_key)
                                if result is not None:
                                    return result
                        return None

                    return find_key_value(root_config, key) or match.group(0)

                return re.sub(r'\{(\w+)\}', replacer, obj)
            return obj

        # Apply recursive placeholder replacement
        processed_config = replace_placeholders(config_data, config_data)
        return self._dict_to_namespace(processed_config)

    def _dict_to_namespace(self, d):
        """Convert dictionary to SimpleNamespace recursively."""
        if isinstance(d, dict):
            return SimpleNamespace(**{k: self._dict_to_namespace(v) for k, v in d.items()})
        return d

    def __getattr__(self, name):
        """Allow direct access to root keys."""
        return getattr(self._data, name)
