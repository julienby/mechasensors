from mechareader import Config

# Exemple d'utilisation
# Charger la configuration
mydevice = Config("config.json")

def get_instance_by_name(name):
    """
    Récupère l'instance d'un objet à partir de son nom (chaîne de texte).

    :param name: Le nom de l'objet en tant que chaîne.
    :return: L'instance de l'objet si trouvée, sinon lève une exception.
    """
    if name in globals():
        return globals()[name]
    else:
        raise NameError(f"L'objet '{name}' n'existe pas dans l'espace global.")


# Exemple d'accès
<<<<<<< HEAD
print(mydevice.node.specs.software.name)  # Devrait afficher "NodeControllerClient"
print(mydevice.node.id)  # Devrait afficher "hostname_TERRAIN001"
print(mydevice.node.communication.ping.cmd)  # Devrait afficher "curl https://status.server.com/check"
print(mydevice.node.host)  # Devrait afficher "curl https://status.server.com/check"
print(mydevice.node.specs.software.long_name)
=======
print(icaging.node.specs.software.name)  # Devrait afficher "NodeControllerClient"
print(icaging.node.id)  # Devrait afficher "hostname_TERRAIN001"
print(icaging.node.communication.ping.cmd)  # Devrait afficher "curl https://status.server.com/check"
print(icaging.node.host)  # Devrait afficher "curl https://status.server.com/check"
print(icaging.node.specs.software.long_name)
print(icaging.node.data.local.path)  # Devrait afficher "curl https://status.server.com/check"

# Liste des chemins à afficher
paths = [
    'icaging.node.specs.software.name',
    'icaging.node.id',
]

def resolve_path_recursively(obj, path):
    """
    Résout récursivement un chemin donné sous forme de chaîne pour accéder aux attributs d'un objet
    ou aux clés d'un dictionnaire.

    :param obj: L'objet ou le dictionnaire de base.
    :param path: Le chemin sous forme de chaîne, séparé par des points.
    :return: La valeur trouvée au chemin spécifié.
    :raises AttributeError, KeyError: Si un niveau du chemin est introuvable.
    """
    keys = path.split(".")  # Divise le chemin en niveaux
    for key in keys:
        if isinstance(obj, dict):  # Si l'objet est un dictionnaire
            obj = obj[key]
        else:  # Si l'objet est une instance de classe
            obj = getattr(obj, key)
    return obj


#print(get_instance_by_name("icaging"))
#print(getattr(icaging, "node"))

print(resolve_path_recursively(get_instance_by_name("icaging"), "node.id"))
print(icaging.node.id)
>>>>>>> e202169 (documentation et prettyprinter)
