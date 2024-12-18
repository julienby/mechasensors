# mechasensors Configuration JSON pour le Pilotage des Capteurs Connectés

Mecha Sensors

Ce fichier JSON définit la configuration des capteurs connectés, pilotés via des microcontrôleurs Arduino et Raspberry Pi. Il contient les informations nécessaires pour le fonctionnement local, la communication avec le cloud, et les déclencheurs d'actions automatisées.

---

## Table des matières
- [Structure du fichier JSON](#structure-du-fichier-json)
- [Description des Sections](#description-des-sections)
  - [Node](#node)
  - [Communication](#communication)
  - [Location](#location)
  - [Measurement](#measurement)
  - [Data](#data)
  - [Trigger](#triggers)
  - [SensorCard](#sensorcard)
  - [SensorGroup](#sensorgroup)
  - [Sensor](#sensor)
- [Exemple de Fichier JSON](#exemple-de-fichier-json)

---

## Structure du fichier JSON

```plaintext
{
  "nodeController": {
    ...
    "communication": { ... },
    "location": { ... },
    "measurement": { ... },
    "data": { ... },
    "triggers": [ ... ],
    "SensorCards": [ ... ]
  }
}
```

---

## Description des Sections

### Node
- **id** : Identifiant unique du contrôleur. Format `{host}_{dataset_id}`.
- **name** : Nom du contrôleur.
- **description** : Description du contrôleur.
- **host** : Nom du système hôte.
- **dataset_id** : Identifiant du jeu de données.
- **mode** : Mode de fonctionnement (`debug` ou `production`).
- **status** : État actuel du contrôleur (`on` ou `off`).

---

### Communication
- **cloud** : Configuration pour la communication avec le cloud.
  - **api_url** : URL de l'API du service cloud.
  - **api_key** : Clé d'accès pour l'API.
- **local** : Configuration pour la communication locale.
  - **api_url** : URL de l'interface locale.
- **ping** : Paramètres pour vérifier la disponibilité du réseau.
  - **url** : URL pour vérifier le statut.
  - **crontab** : Expression cron pour planifier les vérifications.
  - **cmd** : Commande exécutée pour le test.

---

### Location
- **geo** : Coordonnées géographiques.
  - **latitude** : Latitude en degrés.
  - **longitude** : Longitude en degrés.
  - **altitude** : Altitude en mètres.
- **address** : Informations sur l'adresse physique.
  - **building** : Nom ou numéro du bâtiment.
  - **floor** : Étage.
  - **room** : Salle.
  - **zone** : Zone géographique.
  - **postalCode** : Code postal.
  - **city** : Ville.
  - **country** : Pays.
- **indoor** : Indique si le capteur est à l'intérieur (booléen).

---

### Measurement
- **period** : Periode de mesure (ex. `1s`).
- **mode** : Mode de fonctionnement (`slave` ou `master`).

---

### Data
- **remote** : Configuration des synchronisations de données distantes.
  - **id** : Identifiant du serveur distant.
  - **protocol** : Protocole utilisé (ex. `rsync`).
  - **remote_path** : Chemin des données sur le serveur distant.
  - **ssh** : Paramètres de connexion SSH.
    - **user_host** : Identifiant utilisateur et hôte SSH.
    - **command** : Commande pour synchroniser les fichiers.
    - **schedule** : Planification des synchronisations.
- **local** : Chemin local des données.

---

### Trigger
Déclencheurs d'actions en fonction des conditions :
- **condition** : Condition qui déclenche l'action.
  - **type** : Type de condition (ex. `battery_level`, `sensor_value`, `scheduled`).
  - **operator** : Opérateur de comparaison (`greater_than`, `less_than`).
  - **value** : Valeur seuil.
- **action** : Action à effectuer si la condition est remplie.
  - **type** : Type d'action (ex. `sleeping_mode`, `notify`, `restart`).
  - **message** : Message associé à l'action.

---

### SensorCard
Carte connecté au Pi :
- **id** : Identifiant unique de la carte.
- **name** : Nom de la carte.
- **description** : Description de la carte.
- **manufacturer** : Fabricant.
- **model** : Modèle.
- **portConnected** : Informations sur le port.
  - **portType** : Type de port (`usb`, `serial`).
  - **portAdress** : Adresse du port.
  - **baudrate** : Vitesse de transmission.
- **Sensors** : Liste des capteurs.
  - **id** : Identifiant unique du capteur.
  - **type** : Type de capteur (ex. `capteur`, `groupe`).
  - **measurement** : Paramètres de mesure.
    - **type** : Type de mesure (ex. `valvometrie`, `numeric`).
    - **unite** : Unité de la mesure.
    - **format** : Format des données (`int`, `float`).
    - **range** : Plage de mesure.

  ### SensorCards
  List of sensorCard

---

## Exemple de Fichier JSON

```json
{
  "nodeController": {
    "id": "pil-92_TERRAIN001",
    "name": "RPI Pil 92",
    "description": "RPI utilisé pour le terrain",
    "communication": {
      "cloud": {
        "api_url": "https://api.cloudservice.com/v1/control",
        "api_key": "your-cloud-api-key"
      },
      "local": {
        "api_url": "http://localhost:8080/control"
      }
    },
    "location": {
      "geo": {
        "latitude": 48.8588443,
        "longitude": 2.2943506,
        "altitude": 45
      },
      "address": {
        "building": "Building A",
        "floor": "3rd Floor",
        "room": "Room 305",
        "zone": "West Wing",
        "postalCode": "75007",
        "city": "Paris",
        "country": "France"
      }
    },
    "SensorCards": [
      {
        "id": "carte1_acquisition",
        "name": "arduino mega v123",
        "Sensors": [
          {
            "id": "moule1",
            "type": "capteur",
            "measurement": {
              "type": "valvometrie",
              "unite": "Gauss",
              "format": "int",
              "range": "0-1024"
            }
          }
        ]
      }
    ]
  }
}
```

---

### Contribuer
Pour contribuer ou signaler un problème, ouvrez une **issue** ou proposez une **pull request**.
