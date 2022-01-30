from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

# Build list of stations
stations = build_station_list()

print(len(rivers_with_station(stations)))
print(rivers_with_station(stations)[:10])

print(stations_by_river(stations))