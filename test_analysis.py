from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


import datetime
import numpy as np
import math



def test_polyfit():

    stations = build_station_list()
    update_water_levels(stations)

    stationlist=[]

    for i,j in stations_highest_rel_level(stations,5):
        stationlist += [i]

    test_stations = [station for station in stations if station.name in stationlist]

    for station in test_stations:

        # 2 day time interval
        dt = 2
        # polynomial order 4
        p = 4

        dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))

        assert type(polyfit(dates, levels, p)) == tuple #testing that a tuple is the output
        assert len(polyfit(dates, levels, p)[0]) == 4 #verifying that output is polynomial of order 4

test_polyfit()