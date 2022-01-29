from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

# Build list of stations
stations = build_station_list()

def stations_by_distance(stations, p):
    "sort stations by increasing distance from the coordinate p"

    stations_distance = []

    for station in stations:
        stations_distance += (station.name, station.town, haversine(station.coord, p))

    stations_distance = sorted_by_key(stations_distance, 2)

    return stations_distance

print(stations_by_distance(stations, (52.2053, 0.1218)))
