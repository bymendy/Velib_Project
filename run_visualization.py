from app.visualization import (
    plot_station_bikes_over_time,
    plot_capacity_distribution,
    plot_bikes_distribution,
    create_stations_map,
)

if __name__ == "__main__":
    plot_station_bikes_over_time("Saint-Sulpice")
    plot_capacity_distribution()
    plot_bikes_distribution()
    create_stations_map()