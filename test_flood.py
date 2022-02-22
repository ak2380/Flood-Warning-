from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list

def test_2B():

    stations = build_station_list()

    for i in stations_level_over_threshold(stations,0.8):
        assert i[i][1] > i[i+1][1]



test_2B()