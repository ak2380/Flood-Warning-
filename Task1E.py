from floodsystem.stationdata import build_station_list
from collections import Counter

stations = build_station_list()

def rivers_by_station_number(stations):

    rivers_list = []

    for station in stations:
        rivers_list.append(station.river)

    rivers_list.sort()

    rivcount = dict(Counter(rivers_list))

    rivlist = []

    #for key, value in rivcount:
     #   rivlist += (key,value)

    return rivcount

print(rivers_by_station_number(stations))
