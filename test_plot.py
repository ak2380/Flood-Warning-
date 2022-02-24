from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels

import datetime
import numpy as np
import random

def test_2E():

    stations = build_station_list()
    update_water_levels(stations)

    for N in [1, 10, 20, 30]:
        station = stations[N]
        dt = 5
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)


def test_plot_water_level_with_fit():
    p = 4
    stations = build_station_list()
    update_water_levels(stations)

    # choose random stations to generate plots for and visually inspect

    for N in [random.randint(1,100), random.randint(1,100), random.randint(1,100)]:
        station = stations[N]
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, p)

test_plot_water_level_with_fit()
test_2E()