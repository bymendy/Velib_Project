def normalize_boolean(value):
    """
    Convertit les valeurs OUI/NON, 1/0, True/False en booléen Python.
    """
    if isinstance(value, bool):
        return value

    if value is None:
        return None

    value_str = str(value).strip().upper()

    if value_str in {"OUI", "1", "TRUE"}:
        return True
    if value_str in {"NON", "0", "FALSE"}:
        return False

    return None


def extract_station_data(api_data):
    """
    Extrait les informations utiles des stations Vélib.

    Args:
        api_data (dict): données brutes récupérées depuis l'API

    Returns:
        list[dict]: liste de dictionnaires contenant les données utiles
    """
    records = api_data.get("records", [])
    cleaned_data = []

    for record in records:
        fields = record.get("fields", {})
        coordinates = fields.get("coordonnees_geo", [None, None])

        station_info = {
            "station_name": fields.get("name"),
            "station_id": fields.get("stationcode"),
            "capacity": fields.get("capacity"),
            "mechanical_bikes": fields.get("mechanical"),
            "electric_bikes": fields.get("ebike"),
            "total_bikes_available": fields.get("numbikesavailable"),
            "available_docks": fields.get("numdocksavailable"),
            "latitude": coordinates[0] if len(coordinates) > 0 else None,
            "longitude": coordinates[1] if len(coordinates) > 1 else None,
            "commune_code": fields.get("code_insee_commune"),
            "commune_name": fields.get("nom_arrondissement_communes"),
            "is_installed": normalize_boolean(fields.get("is_installed")),
            "is_renting": normalize_boolean(fields.get("is_renting")),
            "is_returning": normalize_boolean(fields.get("is_returning")),
            "updated_at": fields.get("duedate")
        }

        cleaned_data.append(station_info)

    return cleaned_data