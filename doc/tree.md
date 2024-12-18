
Configuration Tree
==================================================
Configuration
|-- file_path
|   +-- config.json
+-- _data
    +-- node
        |-- id
        |   +-- hostname_TERRAIN001
        |-- name
        |   +-- RPI XYZ
        |-- description
        |   +-- Description RPI XYZ
        |-- host
        |   +-- hostname
        |-- dataset_id
        |   +-- TERRAIN001
        |-- mode
        |   +-- debug production
        |-- status
        |   +-- on off
        |-- communication
        |   |-- cloud
        |   |   |-- api_url
        |   |   |   +-- https://api.cloudservice.com/v1/control
        |   |   +-- api_key
        |   |       +-- your-cloud-api-key
        |   |-- local
        |   |   +-- api_url
        |   |       +-- http://localhost:8080/control
        |   +-- ping
        |       |-- url
        |       |   +-- https://status.server.com/check
        |       |-- crontab
        |       |   +-- /5 * * * *
        |       +-- cmd
        |           +-- curl https://status.server.com/check
        |-- specs
        |   |-- software
        |   |   |-- name
        |   |   |   +-- NodeControllerClient
        |   |   |-- version
        |   |   |   +-- 1.2.3
        |   |   |-- git
        |   |   |   +-- https://github.com/username/NodeControllerClient
        |   |   +-- long_name
        |   |       +-- NodeControllerClient - 1.2.3
        |   +-- hardware
        |       |-- name
        |       |   +-- Raspberry Pi
        |       |-- version
        |       |   +-- pi3
        |       +-- powerSource
        |           +-- Battery
        |-- location
        |   |-- geo
        |   |   |-- latitude
        |   |   |   +-- 48.8588443
        |   |   |-- longitude
        |   |   |   +-- 2.2943506
        |   |   |-- altitude
        |   |   |   +-- 45
        |   |   +-- unit
        |   |       +-- meters
        |   |-- address
        |   |   |-- building
        |   |   |   +-- Building A
        |   |   |-- floor
        |   |   |   +-- 3rd Floor
        |   |   |-- room
        |   |   |   +-- Room 305
        |   |   |-- zone
        |   |   |   +-- West Wing
        |   |   |-- postalCode
        |   |   |   +-- 75007
        |   |   |-- city
        |   |   |   +-- Paris
        |   |   +-- country
        |   |       +-- France
        |   |-- description
        |   |   +-- Sensor located in the west wing of Building A, 3rd floor, Room 305.
        |   +-- indoor
        |       +-- True
        |-- measurement
        |   |-- period
        |   |   +-- 1s
        |   +-- mode
        |       +-- slave | master
        |-- data
        |   |-- remote
        |   |   +-- Item 1
        |   |       |-- id
        |   |       |   +-- username@serveur.com
        |   |       |-- protocol
        |   |       |   +-- rsync
        |   |       |-- remote_path
        |   |       |   +-- /home/icaging/icaging-litis/{hostname}
        |   |       +-- ssh
        |   |           |-- user_host
        |   |           |   +-- username@serveur.com
        |   |           |-- command
        |   |           |   +-- rsync -av --include='*_{dataset_id}_*.csv' {local_data_path}/ {user_host}:{remote_path}
        |   |           +-- schedule
        |   |               +-- */15 * * * *
        |   +-- local
        |       +-- path
        |           +-- data/
        |-- triggers
        |   |-- Item 1
        |   |   |-- condition
        |   |   |   |-- type
        |   |   |   |   +-- battery_level
        |   |   |   |-- from
        |   |   |   |   +-- sensor_battery1
        |   |   |   |-- operator
        |   |   |   |   +-- less_than
        |   |   |   |-- value
        |   |   |   |   +-- 10
        |   |   |   +-- unit
        |   |   |       +-- percent
        |   |   +-- action
        |   |       |-- type
        |   |       |   +-- sleeping_mode
        |   |       |-- target
        |   |       |   +-- self
        |   |       +-- message
        |   |           +-- Battery level is critically low. Shutting down.
        |   |-- Item 2
        |   |   |-- condition
        |   |   |   |-- type
        |   |   |   |   +-- sensor_value
        |   |   |   |-- from
        |   |   |   |   +-- sensor-001
        |   |   |   |-- operator
        |   |   |   |   +-- greater_than
        |   |   |   |-- value
        |   |   |   |   +-- 75
        |   |   |   +-- unit
        |   |   |       +-- Celsius
        |   |   +-- action
        |   |       |-- type
        |   |       |   +-- notify
        |   |       |-- target
        |   |       |   +-- arduino-001
        |   |       +-- message
        |   |           +-- Temperature exceeds safe threshold.
        |   |-- Item 3
        |   |   |-- condition
        |   |   |   |-- type
        |   |   |   |   +-- scheduled
        |   |   |   +-- datetime
        |   |   |       +-- 2024-10-16T08:30:00Z
        |   |   +-- action
        |   |       |-- type
        |   |       |   +-- restart
        |   |       |-- target
        |   |       |   +-- self
        |   |       |-- status
        |   |       |   +-- restarting
        |   |       +-- message
        |   |           +-- Restarting system.
        |   |-- Item 4
        |   |   |-- condition
        |   |   |   |-- type
        |   |   |   |   +-- once
        |   |   |   +-- datetime
        |   |   |       +-- now
        |   |   +-- action
        |   |       |-- type
        |   |       |   +-- restart
        |   |       |-- target
        |   |       |   +-- self
        |   |       |-- status
        |   |       |   +-- restarting
        |   |       +-- message
        |   |           +-- Restarting system.
        |   +-- Item 5
        |       |-- condition
        |       |   |-- type
        |       |   |   +-- once
        |       |   +-- datetime
        |       |       +-- now
        |       +-- action
        |           |-- type
        |           |   +-- shutdown
        |           |-- target
        |           |   +-- self
        |           |-- status
        |           |   +-- shutdown
        |           +-- message
        |               +-- Restarting system.
        +-- SensorCards
            +-- Item 1
                |-- id
                |   +-- carte1_acquisition
                |-- name
                |   +-- arduino mega v123
                |-- description
                |   +-- A sensor measuring ambient temperature
                |-- manufacturer
                |   +-- Arduino
                |-- model
                |   +-- Mega V2
                |-- port
                |   |-- type
                |   |   +-- usb
                |   |-- adress
                |   |   +-- /dev/ttyACM0
                |   |-- baudrate
                |   |   +-- 9600
                |   +-- status
                |       +-- on
                |-- measurementPeriod
                |   +-- 1s
                |-- measurementMode
                |   +-- ondemand
                |-- software
                |   |-- name
                |   |   +-- SensorController
                |   |-- version
                |   |   +-- 0.9.5
                |   +-- git
                |       +-- https://github.com/username/SensorController
                |-- Sensors
                |   |-- Item 1
                |   |   |-- id
                |   |   |   +-- moule1
                |   |   |-- description
                |   |   |   +--
                |   |   |-- type
                |   |   |   +-- capteur
                |   |   |-- fabricant
                |   |   |   +--
                |   |   |-- measurement
                |   |   |   |-- type
                |   |   |   |   +-- valvometrie
                |   |   |   |-- unite
                |   |   |   |   +-- Gauss
                |   |   |   |-- format
                |   |   |   |   +-- int
                |   |   |   |-- OperationgRange
                |   |   |   |   |-- minValue
                |   |   |   |   |   +-- 0
                |   |   |   |   +-- maxValue
                |   |   |   |       +-- 1024
                |   |   |   +-- read_frequency
                |   |   |       +-- 1Hz
                |   |   +-- physicaladress
                |   |       |-- type
                |   |       |   +-- analog
                |   |       +-- adresse
                |   |           +-- A01
                |   |-- Item 2
                |   |   |-- id
                |   |   |   +-- moule2
                |   |   |-- description
                |   |   |   +--
                |   |   |-- fabricant
                |   |   |   +--
                |   |   |-- status
                |   |   |   +-- on/off
                |   |   |-- measurement
                |   |   |   |-- type
                |   |   |   |   +-- valvometrie
                |   |   |   |-- unite
                |   |   |   |   +-- Gauss
                |   |   |   |-- format
                |   |   |   |   +-- int
                |   |   |   |-- range
                |   |   |   |   +-- [0-1024]
                |   |   |   +-- read_frequency
                |   |   |       +-- 1s
                |   |   +-- physicaladress
                |   |       |-- type
                |   |       |   +-- analog
                |   |       +-- adresse
                |   |           +-- A01
                |   |-- Item 3
                |   |   |-- id
                |   |   |   +-- moule2
                |   |   |-- description
                |   |   |   +--
                |   |   |-- fabricant
                |   |   |   +--
                |   |   |-- measurement
                |   |   |   |-- type
                |   |   |   |   +-- valvometrie
                |   |   |   |-- unite
                |   |   |   |   +-- Gauss
                |   |   |   |-- format
                |   |   |   |   +-- int
                |   |   |   |-- range
                |   |   |   |   +-- [0-1024]
                |   |   |   +-- read_frequency
                |   |   |       +-- 1s
                |   |   +-- physicaladress
                |   |       |-- type
                |   |       |   +-- analog
                |   |       +-- adresse
                |   |           +-- A01
                |   |-- Item 4
                |   |   |-- id
                |   |   |   +-- moule2
                |   |   |-- description
                |   |   |   +--
                |   |   |-- fabricant
                |   |   |   +--
                |   |   |-- measurement
                |   |   |   |-- type
                |   |   |   |   +-- valvometrie
                |   |   |   |-- unite
                |   |   |   |   +-- Gauss
                |   |   |   |-- format
                |   |   |   |   +-- int
                |   |   |   |-- range
                |   |   |   |   +-- [0-1024]
                |   |   |   +-- read_frequency
                |   |   |       +-- 1s
                |   |   +-- physicaladress
                |   |       |-- type
                |   |       |   +-- analog
                |   |       +-- adresse
                |   |           +-- A01
                |   +-- Item 5
                |       |-- id
                |       |   +-- sonde_ph
                |       |-- description
                |       |   +-- Sonde Ph
                |       |-- fabricant
                |       |   +-- ABC
                |       |-- measurement
                |       |   |-- type
                |       |   |   +-- Ph
                |       |   |-- unite
                |       |   |   +-- ph
                |       |   |-- format
                |       |   |   +-- int
                |       |   |-- range
                |       |   |   +-- [0-14]
                |       |   +-- read_frequency
                |       |       +-- 1Hz
                |       +-- physicaladress
                |           |-- type
                |           |   +-- analog
                |           +-- adresse
                |               +-- A01
                +-- SensorGroups
                    +-- Item 1
                        |-- id
                        |   +-- sensor_ph_pression_temp1
                        |-- marque
                        |   +-- marque capteur
                        |-- actif
                        |   +-- true
                        |-- descripton
                        |   +--
                        |-- serie
                        |   +--
                        |-- provider
                        |   +--
                        |-- adressephysique
                        |   |-- type
                        |   |   +-- analogique
                        |   +-- adresse
                        |       +-- A01
                        +-- Sensors
                            |-- Item 1
                            |   |-- id
                            |   |   +-- ph
                            |   |-- description
                            |   |   +-- Sonde Ph
                            |   |-- type
                            |   |   +-- sensor
                            |   |-- fabricant
                            |   |   +-- XYZ
                            |   |-- measurement
                            |   |   |-- type
                            |   |   |   +-- numeric
                            |   |   |-- unite
                            |   |   |   +-- ph
                            |   |   |-- format
                            |   |   |   +-- int
                            |   |   |-- OperationgRange
                            |   |   |   |-- minValue
                            |   |   |   |   +-- 0
                            |   |   |   +-- maxValue
                            |   |   |       +-- 14
                            |   |   +-- read_frequency
                            |   |       +-- 1s
                            |   +-- physicaladress
                            |       |-- type
                            |       |   +-- analog
                            |       +-- adresse
                            |           +-- A01
                            |-- Item 2
                            |   |-- id
                            |   |   +-- pression
                            |   |-- description
                            |   |   +-- Capteur de pression
                            |   |-- type
                            |   |   +-- sensor
                            |   |-- fabricant
                            |   |   +-- ABC
                            |   |-- measurement
                            |   |   |-- type
                            |   |   |   +-- numeric
                            |   |   |-- unite
                            |   |   |   +-- P°
                            |   |   |-- format
                            |   |   |   +-- int
                            |   |   |-- OperationgRange
                            |   |   |   |-- minValue
                            |   |   |   |   +-- 0
                            |   |   |   +-- maxValue
                            |   |   |       +-- 1024
                            |   |   +-- read_frequency
                            |   |       +-- 1h
                            |   +-- physicaladress
                            |       |-- type
                            |       |   +-- analog
                            |       +-- adresse
                            |           +-- B01
                            +-- Item 3
                                |-- id
                                |   +-- temp1
                                |-- description
                                |   +--
                                |-- type
                                |   +-- capteur
                                |-- fabricant
                                |   +--
                                |-- measurement
                                |   |-- type
                                |   |   +-- numeric
                                |   |-- unite
                                |   |   +-- temp
                                |   |-- format
                                |   |   +-- float
                                |   |-- OperationgRange
                                |   |   |-- minValue
                                |   |   |   +-- 0
                                |   |   +-- maxValue
                                |   |       +-- 100
                                |   +-- read_frequency
                                |       +-- 1s
                                +-- physicaladress
                                    |-- type
                                    |   +-- analog
                                    +-- adresse
                                        +-- A01

End of Configuration Tree
==================================================
