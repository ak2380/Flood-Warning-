from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
import matplotlib
import numpy as np

#rating risk at ‘severe’, ‘high’, ‘moderate’ or ‘low’

#water level at a station rising/falling is assessed by taking derivatives
#consider how many "ranges" the current water level is above the normal average water level.

# risk categories:
predicted_rise_stations = []
severe_stations = []

# Define n number of most at risk stations
n = 20

stations = build_station_list()
update_water_levels(stations)

stationlist=[]

for i,j in stations_highest_rel_level(stations,n):
    stationlist += [i]

print(stationlist)

high_level_stations = [station for station in stations if station.name in stationlist]

for station in high_level_stations:

    # 2 day time interval
    dt = 2
    # polynomial order 4
    p = 4

    dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))

    poly, shift = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)

    # get the end plot data point
    current_time = max(x - shift)

    # predict the actual water level tomorrow by subbing into polynomial
    prediction = poly(current_time + 1)

    # Convert all levels to relative
    rel_current_level = station.relative_water_level()
    rel_predicted_level = (prediction - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])
    rel_rise = rel_predicted_level - rel_current_level

    d_poly = poly.deriv()
    d2_poly = poly.deriv(2)

    current_d = d_poly(current_time)
    current_d2 = d2_poly(current_time)

    #weighting of risk factors
    rel_rise_weighting = 0.5
    d_weighting = 0.4
    d2_weighting = 0.1

    risk = (rel_rise * rel_rise_weighting) + (current_d *  d_weighting) + (current_d2 *  d2_weighting)

    if rel_rise > 0: #i.e. water level is rising
        predicted_rise_stations.append([station.name, rel_rise])
        print("Station at risk: " + str(station.name))
        print("Relative current water level: " + str(rel_current_level))
        print("Relative predicted water level: " + str(rel_predicted_level))
        print("Rise in relative water levels: " + str(rel_rise))
        print("Current rate of rise (First derivative) " + str(rel_rise))
        print("Current rate of rise in rate of rise (Second derivative) " + str(rel_rise))
        print("Weighted risk: " + str(risk))
        print("")