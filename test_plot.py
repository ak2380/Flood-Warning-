from floodsystem.stationdata import build_station_list, update_water_levels


from floodsystem.plot import plot_water_levels

def test_2E():

    stations = build_station_list
    update_water_levels(stations)
    
    for station in stations:


test_2E()