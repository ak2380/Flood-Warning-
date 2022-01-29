from floodsystem.stationdata import build_station_list

# Build list of stations
stations = build_station_list()

def rivers_with_station(stations):
    "returns a container with the names of the rivers with a monitoring station"

    rivers_list = []

    for station in stations:
        if station.river not in rivers_list: # if name is not already in list, add it to list
            rivers_list.append(station.river)

    return (rivers_list)

print(rivers_with_station(stations))


def stations_by_river(stations):