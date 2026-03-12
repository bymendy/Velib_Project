from app.api_client import fetch_velib_data, save_raw_data
from app.data_cleaning import extract_station_data
from app.csv_export import save_to_csv, append_to_history
from app.monitoring import monitor_station


def run_data_pipeline():
    """
    Étape 1 : récupération des données et création du CSV
    """
    api_data = fetch_velib_data()
    save_raw_data(api_data)

    cleaned_data = extract_station_data(api_data)

    df = save_to_csv(cleaned_data)

    # ajout dans l'historique pour suivre l'évolution dans le temps
    append_to_history(cleaned_data)

    print("Traitement terminé avec succès.")
    print(df.head())


def run_monitoring():
    """
    Étape 2 : surveillance d'une station Vélib
    """
    monitor_station()


if __name__ == "__main__":
    run_data_pipeline()