from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def test_2B():

    stations = build_station_list()
    update_water_levels(stations)

    assert stations_level_over_threshold(stations,0.8)[0][1] > stations_level_over_threshold(stations,0.8)[-1][1]

def test_2C():

    stations = build_station_list()
    update_water_levels(stations)

    assert stations_highest_rel_level(stations,10)[0][1] > stations_highest_rel_level(stations,10)[-1][1]
    assert len(stations_highest_rel_level(stations,10)) == 10
    

test_2B()
test_2C()