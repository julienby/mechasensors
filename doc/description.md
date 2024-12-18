# Documentation des Métadonnées du Dispositif d'Enregistrement de Données

## Informations générales sur le noeud

- **ID** : `{node.host}_{node.dataset_id}`
- **Nom** : `RPI XYZ`
- **Description** : `Description RPI XYZ`
- **Hôte** : `hostname`
- **Dataset ID** : `TERRAIN001`
- **Mode** : `debug` | `production`
- **Statut** : `on` | `off`

---

## Communication

### Cloud
- **API URL** : `https://api.cloudservice.com/v1/control`
- **API Key** : `your-cloud-api-key`

### Local
- **API URL** : `http://localhost:8080/control`

### Ping
- **URL** : `https://status.server.com/check`
- **Crontab** : `/5 * * * *`
- **Commande** : `curl {node.communication.ping.url}`

---

## Spécifications

### Logiciel
- **Nom** : `NodeControllerClient`
- **Version** : `1.2.3`
- **GitHub** : [NodeControllerClient](https://github.com/username/NodeControllerClient)
- **Nom long** : `{node.specs.software.name} - {node.specs.software.version}`

### Matériel
- **Nom** : `Raspberry Pi`
- **Version** : `pi3`
- **Source d'alimentation** : `Battery`

---

## Localisation

### Coordonnées géographiques
- **Latitude** : `48.8588443`
- **Longitude** : `2.2943506`
- **Altitude** : `45 meters`

### Adresse
- **Bâtiment** : `Building A`
- **Étage** : `3rd Floor`
- **Salle** : `Room 305`
- **Zone** : `West Wing`
- **Code postal** : `75007`
- **Ville** : `Paris`
- **Pays** : `France`

### Description
- `Sensor located in the west wing of Building A, 3rd floor, Room 305.`

### Intérieur/Extérieur
- **Indoor** : `true`

---

## Mesures

- **Période de mesure** : `1s`
- **Mode** : `slave` | `master`

---

## Données

### Distant
- **ID** : `username@serveur.com`
- **Protocole** : `rsync`
- **Chemin distant** : `/home/icaging/icaging-litis/{hostname}`
- **SSH** :
  - **Utilisateur et Hôte** : `username@serveur.com`
  - **Commande** : `rsync -av --include='*_{dataset_id}_*.csv' {local_data_path}/ {user_host}:{remote_path}`
  - **Planification** : `*/15 * * * *`

### Local
- **Chemin** : `data/`

---

## Déclencheurs

### Déclencheur 1 : Niveau de batterie
- **Condition** :
  - Type : `battery_level`
  - Capteur : `sensor_battery1`
  - Opérateur : `less_than`
  - Valeur : `10%`
- **Action** :
  - Type : `sleeping_mode`
  - Cible : `self`
  - Message : `Battery level is critically low. Shutting down.`

### Déclencheur 2 : Valeur du capteur
- **Condition** :
  - Type : `sensor_value`
  - Capteur : `sensor-001`
  - Opérateur : `greater_than`
  - Valeur : `75°C`
- **Action** :
  - Type : `notify`
  - Cible : `arduino-001`
  - Message : `Temperature exceeds safe threshold.`

### Déclencheur 3 : Planifié
- **Condition** :
  - Type : `scheduled`
  - Date et heure : `2024-10-16T08:30:00Z`
- **Action** :
  - Type : `restart`
  - Cible : `self`
  - Statut : `restarting`
  - Message : `Restarting system.`

---

## Cartes Capteurs

### Carte 1 : Arduino Mega V123
- **ID** : `carte1_acquisition`
- **Nom** : `arduino mega v123`
- **Description** : `A sensor measuring ambient temperature`
- **Fabricant** : `Arduino`
- **Modèle** : `Mega V2`
- **Port** :
  - Type : `usb`
  - Adresse : `/dev/ttyACM0`
  - Baudrate : `9600`
  - Statut : `on`
- **Période de mesure** : `1s`
- **Mode de mesure** : `ondemand`
- **Logiciel** :
  - Nom : `SensorController`
  - Version : `0.9.5`
  - GitHub : [SensorController](https://github.com/username/SensorController)

---

### Capteurs associés

#### Capteur 1 : Moule1
- **Type** : `capteur`
- **Mesure** :
  - Type : `valvometrie`
  - Unité : `Gauss`
  - Format : `int`
  - Plage : `[0-1024]`
  - Fréquence de lecture : `1Hz`
- **Adresse physique** :
  - Type : `analog`
  - Adresse : `A01`

#### Capteur 2 : Sonde pH
- **Description** : `Sonde Ph`
- **Fabricant** : `ABC`
- **Mesure** :
  - Type : `Ph`
  - Unité : `ph`
  - Format : `int`
  - Plage : `[0-14]`
  - Fréquence de lecture : `1Hz`
- **Adresse physique** :
  - Type : `analog`
  - Adresse : `A01`

---

## Groupes de Capteurs

### Groupe : Sensors pH, Pression, Température
- **ID** : `sensor_ph_pression_temp1`
- **Marque** : `marque capteur`
- **Actif** : `true`
- **Capteurs** :
  - **pH** :
    - Type : `numeric`
    - Unité : `ph`
    - Plage : `[0-14]`
    - Fréquence : `1s`
  - **Pression** :
    - Type : `numeric`
    - Unité : `P°`
    - Plage : `[0-1024]`
    - Fréquence : `1h`
  - **Température** :
    - Type : `numeric`
    - Unité : `temp`
    - Plage : `[0-100]`
    - Fréquence : `1s`
