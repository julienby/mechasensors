from mechareader import Config

# Exemple d'utilisation
# Charger la configuration
mydevice = Config("config.json")

# Exemple d'accès
print(mydevice.node.specs.software.name)  # Devrait afficher "NodeControllerClient"
print(mydevice.node.id)  # Devrait afficher "hostname_TERRAIN001"
print(mydevice.node.communication.ping.cmd)  # Devrait afficher "curl https://status.server.com/check"
print(mydevice.node.host)  # Devrait afficher "curl https://status.server.com/check"
print(mydevice.node.specs.software.long_name)
