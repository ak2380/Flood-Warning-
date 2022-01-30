# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_1F():

    stations = build_station_list()

    assert type(inconsistent_typical_range_stations(stations)) == list #testing that a list is the output
    test_list = []
    for station in stations:
        if station.typical_range != None:
            if station.typical_range[0] > station.typical_range[1]:
                test_list.append(station.name)
        elif station.typical_range == None:
            test_list.append(station.name)
    assert sorted(test_list) == inconsistent_typical_range_stations(stations) 

test_1F()