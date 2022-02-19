from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
import matplotlib

#rating risk at ‘severe’, ‘high’, ‘moderate’ or ‘low’

#water level at a station rising/falling is assessed by taking derivatives
#consider how many "ranges" the current water level is above the normal average water level.

stations = build_station_list()
update_water_levels(stations)

# Define N number of most at risk stations
n = 20

high_level_stations = stations_highest_rel_level(stations, n)

# risk categories:
predicted_rise_stations = []
severe_stations = []

for station in high_level_stations:

    # 2 day time interval
    dt = 2
    # polynomial order 4
    p = 4

    dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))

    poly, shift = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)

    # get the end plot data point
    current = max(x - shift)

    # predict the actual water level tomorrow by subbing into polynomial
    prediction = poly(current + 1)

    rel_current_level = station.relative_water_level()
    rel_predicted_level = (prediction - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])


    rel_rise = rel_predicted_level - rel_current_level

    if rel_rise > 0: #i.e. water level is rising
        predicted_rise_stations.append([station.name, rel_rise])
        print("Station at risk: " + str(station.name))
        print("Relative current water level: " + str(rel_current_level))
        print("Relative predicted water level: " + str(rel_predicted_level))
        print("Rise in relative water levels: " + str(rel_rise))