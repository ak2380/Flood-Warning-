from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

stations = build_station_list()

def stations_by_distance(stations, p):
    "sort stations by increasing distance from the coordinate p"

    stations_distance = []

    for station in stations:
        stations_distance += (station.name, station.town, haversine(station.coord, p))

    stations_distance = sorted_by_key(stations_distance, 2, reverse=False)

    return stations_distance

print(stations_by_distance(stations, (52.2053, 0.1218)))