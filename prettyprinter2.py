from mechareader import Config
import json
from anytree import Node, RenderTree, AsciiStyle
import re

commands = []

def filter_and_sort_by_regex(input_list, regex_pattern):
    """
    Filtre une liste en fonction d'un pattern regex et trie les résultats par ordre alphabétique.

    :param input_list: La liste d'entrée à filtrer (list of str).
    :param regex_pattern: Le pattern regex utilisé pour le filtrage (str).
    :return: Une liste triée contenant uniquement les éléments correspondant au pattern.
    """
    # Filtrer les éléments avec la regex
    filtered_list = [item for item in input_list if re.search(regex_pattern, item)]

    # Trier par ordre alphabétique
    sorted_list = sorted(filtered_list)

    return sorted_list

def build_tree(data, parent=None, path="icaging"):
    """Recursively build a tree structure from the data and collect access commands."""
    if isinstance(data, dict):
        for key, value in data.items():
            node = Node(key, parent=parent)
            new_path = f"{path}.{key}"
            build_tree(value, parent=node, path=new_path)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            node = Node(f"Item {index + 1}", parent=parent)
            new_path = f"{path}[{index}]"
            build_tree(item, parent=node, path=new_path)
    else:
        Node(str(data), parent=parent)
        commands.append(f"{path} -> {data}")

class ConfigTreeViewer:
    def __init__(self, config_path):
        self.config = Config(config_path)

    def display_tree(self, branch_path=None):
        print("\nConfiguration Tree")
        print("=" * 50)

        # Convert the Config object to a dictionary
        config_dict = json.loads(json.dumps(self.config, default=lambda o: o.__dict__))
        root = Node("Configuration")
        build_tree(config_dict, parent=root)

        if branch_path:
            # Navigate to the specified branch
            branch = root
            for part in branch_path.split("."):
                branch = next((child for child in branch.children if child.name == part), None)
                if branch is None:
                    print(f"Branch '{branch_path}' not found.")
                    return
            for pre, fill, node in RenderTree(branch, style=AsciiStyle()):
                print(f"{pre}{node.name}")
        else:
            for pre, fill, node in RenderTree(root, style=AsciiStyle()):
                print(f"{pre}{node.name}")

        print("\nEnd of Configuration Tree")
        print("=" * 50)

    def display_commands(self):
        print("\nAccess Commands")
        print("=" * 50)
        dico = []

        def generate_commands(data, path="icaging"):
            if isinstance(data, dict):
                for key, value in data.items():
                    generate_commands(value, f"{path}.{key}")
            elif isinstance(data, list):
                for index, item in enumerate(data):
                    generate_commands(item, f"{path}[{index}]")
            else:
                #path = path.replace("._data", "")
                dico.append(path)
                print(f"{path}")

        config_dict = json.loads(json.dumps(self.config, default=lambda o: o.__dict__))
        #print(config_dict)
        generate_commands(config_dict["_data"])
        ## Appeler la fonction
        #regex_pattern = r'\.communication\.'
        regex_pattern = r'icaging\.node\.SensorCards\[0\]\.SensorGroups\[\d+\]\..*\.id'

        result = filter_and_sort_by_regex(dico, regex_pattern)
        print(result)
        print("\nEnd of Access Commands")
        print("=" * 50)


if __name__ == "__main__":
    viewer = ConfigTreeViewer("config.json")
    viewer.display_tree()  # Display the full tree
    #viewer.display_commands()
    #viewer.display_tree()
