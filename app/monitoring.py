import time

from app.api_client import fetch_velib_data
from app.data_cleaning import extract_station_data


CHECK_INTERVAL = 120  # 2 minutes


def find_empty_station(stations):
    """
    Cherche une station qui n'a aucun vélo disponible.
    """
    for station in stations:
        if station["total_bikes_available"] == 0:
            return station
    return None


def monitor_station():
    """
    Trouve une station vide puis la surveille jusqu'à ce qu'un vélo devienne disponible.
    """

    print("Recherche d'une station vide...")

    api_data = fetch_velib_data()
    stations = extract_station_data(api_data)

    station = find_empty_station(stations)

    if station is None:
        print("Aucune station vide trouvée pour le moment.")
        return

    station_name = station["station_name"]
    station_id = station["station_id"]

    print(f"Station vide trouvée : {station_name}")

    previous_bikes = 0

    while True:

        try:
            api_data = fetch_velib_data()
            stations = extract_station_data(api_data)

            # retrouver la même station
            current_station = None
            for s in stations:
                if s["station_id"] == station_id:
                    current_station = s
                    break

            if current_station is None:
                print("Station non trouvée dans les données.")
                return

            bikes = current_station["total_bikes_available"]

            print(f"Station : {station_name} | vélos disponibles : {bikes}")

            if previous_bikes == 0 and bikes > 0:
                print("ALERTE : Un vélo est maintenant disponible !")
                return

            previous_bikes = bikes

        except Exception as error:
            print("Erreur :", error)

        print("Prochaine vérification dans 2 minutes...\n")
        time.sleep(CHECK_INTERVAL)