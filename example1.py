from tkv_reader import Config

# Exemple d'utilisation
# Charger la configuration
icaging = Config("config.json")

# Accéder aux paramètres
#print(icaging.nodeController.specs.software.name)  # "NodeControllerClient"
#print(icaging.nodeController.location.geo.latitude)  # 48.8588443
#print(icaging.nodeController.location.geo.longitude)  # 48.8588443
#print(icaging.nodeController.SensorCards[0].Sensors[0].id)  # "moule1"
# Exemple d'accès
print(icaging.nodeController.specs.software.name)  # Devrait afficher "NodeControllerClient"
print(icaging.nodeController.id)  # Devrait afficher "hostname_TERRAIN001"
print(icaging.nodeController.communication.ping.cmd)  # Devrait afficher "curl https://status.server.com/check"
print(icaging.nodeController.host)  # Devrait afficher "curl https://status.server.com/check"
