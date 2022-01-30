from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
stations = build_station_list()

print(inconsistent_typical_range_stations(stations))