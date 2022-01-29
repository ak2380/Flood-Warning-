from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

# Build list of stations
stations = build_station_list()

print (stations_within_radius(stations, (52.2053, 0.1218), 10))