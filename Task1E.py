from floodsystem.stationdata import build_station_list

stations = build_station_list()

def rivers_by_station_number(stations, N):

    rivers_list = []

    for station in stations:
        rivers_list += station.name

    return rivers_list

print(rivers_by_station_number)
