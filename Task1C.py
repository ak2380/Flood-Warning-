import math
from haversine import haversine

def stations_within_radius(stations, centre, r):
    stations_within_radius_list = []

    for station in stations:
        dist_from_centre = haversine (station.coord, centre)
        if dist_from_centre < r:
            stations_within_radius_list.append(station.name)

    alphabetical_stations_within_radius_list = []
    alphabetical_stations_within_radius_list.insert(0, stations_within_radius_list[0])
    for  i in range (1,len(stations_within_radius_list)):
        n = 0
        while n < len(alphabetical_stations_within_radius_list) and alphabetical_stations_within_radius_list[n] < stations_within_radius_list[i]:
            n = n + 1
        alphabetical_stations_within_radius_list.insert(n, stations_within_radius_list[i])

    return (alphabetical_stations_within_radius_list)


from floodsystem.stationdata import build_station_list
# Build list of stations
stations = build_station_list()

print (stations_within_radius(stations, (52.2053, 0.1218), 10))