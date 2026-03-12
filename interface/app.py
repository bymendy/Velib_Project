from pathlib import Path

import pandas as pd
from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "processed" / "stations_velib.csv"
MAP_PATH = BASE_DIR / "charts" / "stations_map.html"


def load_stations_data():
    if not CSV_PATH.exists():
        return pd.DataFrame()

    return pd.read_csv(CSV_PATH)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/stations")
def stations():
    df = load_stations_data()

    if df.empty:
        return render_template("stations.html", stations=[], total_stations=0)

    stations_data = df.to_dict(orient="records")
    return render_template(
        "stations.html",
        stations=stations_data,
        total_stations=len(stations_data)
    )


@app.route("/dashboard")
def dashboard():
    df = load_stations_data()

    if df.empty:
        stats = {
            "total_stations": 0,
            "total_bikes": 0,
            "total_docks": 0,
            "total_mechanical": 0,
            "total_electric": 0
        }
        map_available = False
    else:
        stats = {
            "total_stations": int(len(df)),
            "total_bikes": int(df["total_bikes_available"].fillna(0).sum()),
            "total_docks": int(df["available_docks"].fillna(0).sum()),
            "total_mechanical": int(df["mechanical_bikes"].fillna(0).sum()),
            "total_electric": int(df["electric_bikes"].fillna(0).sum())
        }
        map_available = MAP_PATH.exists()

    return render_template(
        "dashboard.html",
        stats=stats,
        map_available=map_available
    )


if __name__ == "__main__":
    app.run(debug=True)