# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data."""

from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
from collections import Counter

def stations_by_distance(stations, p):
    "sort stations by increasing distance from the coordinate p"

    stations_distance = []

    for station in stations:
        stations_distance.append((station.name, station.town, haversine(station.coord, p)))

    return sorted_by_key(stations_distance,2)

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


def rivers_by_station_number(stations,N):
    "creates a list of N rivers with the most monitoring stations"
    rivers_list = []

    for station in stations:
        rivers_list.append(station.river)

    rivers_list.sort()

    rivcount = dict(Counter(rivers_list))

    rivlist = []

    for station,number in rivcount.items():
        rivlist.append((station,number))

    return sorted_by_key(rivlist,1,reverse=True)[:N]

