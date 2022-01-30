from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
    "sort stations by increasing distance from the coordinate p"

    stations_distance = []

    for station in stations:
        stations_distance += (station.name, station.town, haversine(station.coord, p))

    return sorted_by_key(stations_distance, 2)

stations = build_station_list()

p = (52.2053, 0.1218)

print(stations_by_distance(stations,p))