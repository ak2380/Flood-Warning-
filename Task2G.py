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

predicted_rise_towns = []

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

    #differentiate computed polynomial
    d_poly = poly.deriv()
    d2_poly = poly.deriv(2)

    #evaluate derivatives at current time
    current_d = d_poly(current_time)
    current_d2 = d2_poly(current_time)

    #weighting of risk factors
    rel_rise_weighting = 0.5
    d_weighting = 0.4
    d2_weighting = 0.1

    risk = (rel_rise * rel_rise_weighting) + (current_d *  d_weighting) + (current_d2 *  d2_weighting)
    
    #sorting calculated risk into set risk boundaries
    if risk <= 10:
        category = "Low"
    elif risk > 10 and risk <= 30:
        category = "Moderate"
    elif risk > 30 and risk <= 60:
        category = "High"
    elif risk > 60:
        category = "Severe"
    
    predicted_rise_towns.append([station.town, risk])
    
    print("Town at risk: " + str(station.town))
    print("Monitoring Station: " + str(station.name))
    print("Relative current water level: " + str(rel_current_level))
    print("Relative predicted water level: " + str(rel_predicted_level))
    print("Rise in relative water levels: " + str(rel_rise))
    print("Current rate of rise (First derivative): " + str(current_d))
    print("Current rate of rise in rate of rise (Second derivative): " + str(current_d2))
    print("Weighted risk: " + str(risk))
    print("Risk Category: " + category)
    print("")