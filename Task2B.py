from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
stations = build_station_list()

print(stations_level_over_threshold(stations, 0.2))

