from pathlib import Path

import pandas as pd


def save_to_csv(data, output_path="data/processed/stations_velib.csv"):
    """
    Sauvegarde les données nettoyées dans un fichier CSV.

    Args:
        data (list[dict]): données nettoyées
        output_path (str): chemin du fichier CSV de sortie
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    return df


def append_to_history(data, output_path="data/history/stations_history.csv"):
    """
    Ajoute les données actuelles dans un fichier historique CSV
    afin de suivre l'évolution des stations dans le temps.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(data)

    # vérifier si le fichier existe déjà
    file_exists = output_file.exists()

    df.to_csv(
        output_file,
        mode="a",
        header=not file_exists,
        index=False,
        encoding="utf-8-sig"
    )

    return df