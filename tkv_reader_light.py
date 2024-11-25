import json
from types import SimpleNamespace

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = self._load_config()

    def _load_config(self):
        """Charge le fichier JSON et le transforme en un objet accessible par attributs."""
        with open(self.file_path, 'r') as f:
            return json.load(f, object_hook=lambda d: SimpleNamespace(**d))

    def __getattr__(self, name):
        """Permet un accès direct aux clés racines."""
        return getattr(self._data, name)


    def __repr__(self):
        """Retourne une représentation du fichier JSON."""
        return self._data.__repr__()
