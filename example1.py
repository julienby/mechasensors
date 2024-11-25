from mechareader import Config

# Exemple d'utilisation
# Charger la configuration
icaging = Config("config.json")

# Exemple d'accès
print(icaging.node.specs.software.name)  # Devrait afficher "NodeControllerClient"
print(icaging.node.id)  # Devrait afficher "hostname_TERRAIN001"
print(icaging.node.communication.ping.cmd)  # Devrait afficher "curl https://status.server.com/check"
print(icaging.node.host)  # Devrait afficher "curl https://status.server.com/check"
print(icaging.node.specs.software.long_name)
