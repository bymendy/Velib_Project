import json
from pathlib import Path

import requests


API_URL = (
    "https://data.opendatasoft.com/api/records/1.0/search/"
    "?dataset=velib-disponibilite-en-temps-reel%40parisdata"
    "&facet=overflowactivation"
    "&facet=creditcard"
    "&facet=kioskstate"
    "&facet=station_state"
)


def fetch_velib_data(start=0, rows=2000):
    """
    Récupère les données Vélib depuis l'API.

    Args:
        start (int): index de départ des résultats
        rows (int): nombre de lignes à récupérer

    Returns:
        dict: réponse JSON de l'API
    """
    params = {
        "start": start,
        "rows": rows
    }

    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()

    return response.json()


def save_raw_data(data, output_path="data/raw/velib_raw.json"):
    """
    Sauvegarde les données brutes dans un fichier JSON.

    Args:
        data (dict): données renvoyées par l'API
        output_path (str): chemin du fichier de sortie
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    try:
        data = fetch_velib_data()
        save_raw_data(data)
        print("Les données brutes ont été enregistrées dans data/raw/velib_raw.json")
    except requests.exceptions.RequestException as error:
        print(f"Erreur lors de la récupération des données : {error}")