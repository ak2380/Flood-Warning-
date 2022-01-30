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

rivers_list = rivers_with_station(stations)
print(len(rivers_list))

alphabetical_rivers_list = []
alphabetical_rivers_list.insert(0, rivers_list[0])
for  i in range (1,len(rivers_list)):
    n = 0
    while n < len(alphabetical_rivers_list) and alphabetical_rivers_list[n] < rivers_list[i]:
        n = n + 1
    alphabetical_rivers_list.insert(n, rivers_list[i])
print(alphabetical_rivers_list[:10]) #prints first 10 rivers alphabetically


def stations_by_river(stations):
    #create a dictionary mapping that maps river names (the ‘key’) to a list of station objects on a given river
    #key -> item
    station_river_dict = {}
    rivers_list = []
    temp_stations_list = []

    for station in stations:
        # Insert river names keys into dictionary
        if station.river not in rivers_list:
            station_river_dict[station.river] = []
            rivers_list.append(station.river)

    for i in range (0,len(rivers_list)):
    # Insert station names list items into dictionary     
        for station in stations:
            if rivers_list[i] == station.river:
                temp_stations_list.append(station.name)
        station_river_dict[rivers_list[i]] = temp_stations_list
        temp_stations_list = []

    return(station_river_dict)

print(stations_by_river(stations))