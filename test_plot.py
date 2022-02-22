from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels

def test_2E():

    stations = build_station_list()
    update_water_levels(stations)

    for N in [1, 10, 20, 30]:
        station = stations[N]
        dt = 5
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)


test_2E()