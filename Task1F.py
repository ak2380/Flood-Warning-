#from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import test
from floodsystem.stationdata import build_station_list
stations = build_station_list()

#print(inconsistent_typical_range_stations(stations))
print(test(stations))