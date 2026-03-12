from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import folium


def ensure_charts_folder():
    Path("charts").mkdir(parents=True, exist_ok=True)


def plot_station_bikes_over_time(
    station_name,
    history_path="data/history/stations_history.csv",
    output_path="charts/station_bikes_over_time.png"
):
    """
    Crée un graphique de l'évolution du nombre de vélos disponibles
    pour une station donnée.
    """
    ensure_charts_folder()

    df = pd.read_csv(history_path)

    if df.empty:
        print("Le fichier d'historique est vide.")
        return

    station_df = df[df["station_name"] == station_name].copy()

    if station_df.empty:
        print(f"Aucune donnée trouvée pour la station : {station_name}")
        return

    station_df["updated_at"] = pd.to_datetime(station_df["updated_at"])
    station_df = station_df.sort_values("updated_at")

    plt.figure(figsize=(10, 5))
    plt.plot(station_df["updated_at"], station_df["total_bikes_available"])
    plt.title(f"Évolution du nombre de vélos - {station_name}")
    plt.xlabel("Temps")
    plt.ylabel("Vélos disponibles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"Graphique enregistré : {output_path}")


def plot_capacity_distribution(
    csv_path="data/processed/stations_velib.csv",
    output_path="charts/station_capacity.png"
):
    """
    Histogramme des capacités des stations.
    """
    ensure_charts_folder()

    df = pd.read_csv(csv_path)

    plt.figure(figsize=(10, 5))
    plt.hist(df["capacity"].dropna(), bins=20)
    plt.title("Distribution de la capacité des stations Vélib")
    plt.xlabel("Capacité")
    plt.ylabel("Nombre de stations")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"Graphique enregistré : {output_path}")


def plot_bikes_distribution(
    csv_path="data/processed/stations_velib.csv",
    output_path="charts/bikes_distribution.png"
):
    """
    Comparaison entre vélos mécaniques et électriques disponibles.
    """
    ensure_charts_folder()

    df = pd.read_csv(csv_path)

    totals = {
        "Mécaniques": df["mechanical_bikes"].fillna(0).sum(),
        "Électriques": df["electric_bikes"].fillna(0).sum()
    }

    plt.figure(figsize=(8, 5))
    plt.bar(totals.keys(), totals.values())
    plt.title("Répartition actuelle des vélos disponibles")
    plt.xlabel("Type de vélo")
    plt.ylabel("Nombre total")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"Graphique enregistré : {output_path}")


def create_stations_map(
    csv_path="data/processed/stations_velib.csv",
    output_path="charts/stations_map.html"
):
    """
    Crée une carte interactive Folium avec les stations Vélib.
    La capacité de la station est affichée dans le popup.
    """
    ensure_charts_folder()

    df = pd.read_csv(csv_path)

    center_lat = df["latitude"].dropna().mean()
    center_lon = df["longitude"].dropna().mean()

    station_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    for _, row in df.iterrows():
        if pd.isna(row["latitude"]) or pd.isna(row["longitude"]):
            continue

        popup_text = (
            f"Station : {row['station_name']}<br>"
            f"ID : {row['station_id']}<br>"
            f"Capacité : {row['capacity']}<br>"
            f"Vélos disponibles : {row['total_bikes_available']}<br>"
            f"Bornettes libres : {row['available_docks']}"
        )

        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=max(3, min(float(row["capacity"]) / 3, 12)) if pd.notna(row["capacity"]) else 4,
            popup=folium.Popup(popup_text, max_width=300),
            fill=True
        ).add_to(station_map)

    station_map.save(output_path)
    print(f"Carte enregistrée : {output_path}")