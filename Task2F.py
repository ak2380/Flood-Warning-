from datetime import datetime, timedelta, date, time

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)
at_risk_stations = stations_highest_rel_level(stations, 5)

dt = 2
p = 4

for station in at_risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt = timedelta(days = dt))
        # print('station.measure_id =', station.measure_id)
        # print('len(dates) =', len(dates))
        # print('len(levels) =', len(levels))
        if len(dates) < 1 or len(levels) < 1:
            print('ERROR: Data missing in ', station.name)
        else:
            plot_water_level_with_fit(station, dates, levels, p)