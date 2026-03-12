# Velib_Project

Projet d'analyse des données en temps réel de l'API Vélib à Paris.

## Objectif du projet

Ce projet a pour but de récupérer, stocker, analyser et visualiser les données des stations Vélib en temps réel.  
Il permet aussi de surveiller la disponibilité des vélos et de mettre en place un système d'alerte lorsqu'une station précédemment vide redevient disponible.

## Fonctionnalités

- récupération des données depuis l'API Vélib
- stockage des données brutes au format JSON
- extraction et nettoyage des informations utiles
- export des données dans un fichier CSV
- suivi de l'état des stations dans le temps
- génération de visualisations
- préparation d'une future interface web

## Structure du projet

```text
velib_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api_client.py
│   ├── data_cleaning.py
│   ├── csv_export.py
│   ├── monitoring.py
│   ├── alerts.py
│   └── visualization.py
│
├── interface/
│   ├── __init__.py
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── stations.html
│   │   └── dashboard.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── script.js
│       └── images/
│
├── data/
│   ├── raw/
│   │   └── velib_raw.json
│   ├── processed/
│   │   └── stations_velib.csv
│   └── history/
│       └── stations_history.csv
│
├── charts/
│   ├── stations_map.png
│   ├── bikes_distribution.png
│   └── station_capacity.png
│
├── notebooks/
│   └── exploration.ipynb
│
├── tests/
│   ├── test_api_client.py
│   ├── test_data_cleaning.py
│   └── test_alerts.py
│
├── config/
│   └── settings.py
│
├── requirements.txt
├── README.md
└── run.py