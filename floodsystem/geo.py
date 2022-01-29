# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data."""

from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list

stations = build_station_list()

def stations_by_distance(stations, p):
    "sort stations by increasing distance from the coordinate p"

    stations_distance = []

    for station in stations:
        stations_distance += (station.name, station.town, haversine(station.coord, p))

    sorted_by_key(stations_distance, 2)

    return stations_distance


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

