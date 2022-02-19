
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations = build_station_list()
update_water_levels(stations)

stationlist=[]

for i,j in stations_highest_rel_level(stations,5):
    stationlist += [i]

print(stationlist)

station_five = [station for station in stations if station.name in stationlist]

for station in station_five:

    dt = 10
    p = 4

    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    plot_water_level_with_fit(station, dates, levels, p)