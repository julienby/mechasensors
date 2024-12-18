from mechareader import Config
import json

def print_structure(data, indent=0):
    """Recursively print the structure of the data."""
    spacing = "  " * indent
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{spacing}- {key}:")
            print_structure(value, indent + 1)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print(f"{spacing}- [Item {index + 1}]:")
            print_structure(item, indent + 1)
    else:
        print(f"{spacing}- {data}")

class PrettyPrinter:
    def __init__(self, config_path):
        self.config = Config(config_path)

    def display(self):
        print("\nConfiguration Overview")
        print("=" * 50)

        # Convert the Config object to a dictionary
        config_dict = json.loads(json.dumps(self.config, default=lambda o: o.__dict__))
        print_structure(config_dict)

        print("\nEnd of Configuration")
        print("=" * 50)

if __name__ == "__main__":
    printer = PrettyPrinter("config.json")
    printer.display()
