from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

# Build list of stations
stations = build_station_list()
print (stations_by_distance(stations, (52.2053, 0.1218)))