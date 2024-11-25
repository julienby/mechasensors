from tkv_reader import Config

# Exemple d'utilisation
# Charger la configuration
icaging = Config("config.json")

# Accéder aux paramètres
print(icaging.nodeController.specs.software.name)  # "NodeControllerClient"
print(icaging.nodeController.location.geo.latitude)  # 48.8588443
print(icaging.nodeController.location.geo.longitude)  # 48.8588443
print(icaging.nodeController.SensorCards[0].Sensors[0].id)  # "moule1"

#print(config)
