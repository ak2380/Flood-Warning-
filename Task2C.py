from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
stations = build_station_list()

update_water_levels(stations)

for i,j in stations_highest_rel_level(stations,10):
    print(i,j)