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
N = 20

# 2 day time interval
dt = 2
# polynomial order 4
p = 4

most_at_risk_stations = stations_highest_rel_level(stations, N)

# risk categories:
severe_stations = []

for station in most_at_risk_stations:
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days = dt))

    poly, shift = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)

    # get the end plot data point
    current = max(x - shift)

    # predict the water level tomorrow by subbing into polynomial
    prediction = poly(current + 1)

    water_level = station.relative_water_level()
    