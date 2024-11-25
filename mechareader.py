import json
from types import SimpleNamespace
import re

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = self._load_config()

    def _resolve_nested_value(self, config, path):
        """Resolve nested path in the configuration."""
        parts = path.split('.')
        current = config

        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
            elif isinstance(current, SimpleNamespace):
                current = getattr(current, part, None)
            else:
                return None

            if current is None:
                return None

        return current

    def _load_config(self):
        """Load JSON and replace placeholders recursively."""
        with open(self.file_path, 'r') as f:
            config_data = json.load(f)

        def replace_placeholders(obj, root_config):
            if isinstance(obj, dict):
                return {k: replace_placeholders(v, root_config) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [replace_placeholders(item, root_config) for item in obj]
            elif isinstance(obj, str):
                def replacer(match):
                    nested_key = match.group(1)
                    # Special case for top-level nodeController
                    if not '.' in nested_key:
                        nested_key = f'nodeController.{nested_key}'

                    resolved_value = self._resolve_nested_value(root_config, nested_key)
                    return str(resolved_value) if resolved_value is not None else match.group(0)

                return re.sub(r'\{([^}]+)\}', replacer, obj)
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
