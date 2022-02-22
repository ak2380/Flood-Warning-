from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels

import datetime
import numpy as np
import math



def test_polyfit():
    p = 4
    test_station = build_station_list()[0]
    dates, levels = fetch_measure_levels(test_station.measure_id, dt=datetime.timedelta(days=2))
    poly, d0 = polyfit(dates, levels, p)
    assert type(polyfit(dates, levels, p)) == tuple #testing that a tuple is the output
    assert polyfit(dates, levels, p) == 'River Thames' #verifying that River Thames is the closest river

test_polyfit()