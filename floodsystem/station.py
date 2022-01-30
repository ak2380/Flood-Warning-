# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    def test(self): #test
        return(self.typical_range)

    def typical_range_consistent(self): #Task 1F a
        # the range is said to be inconsistent if:
        # (i) no data is available; or 
        # (ii) the reported typical high range is less than the reported typical low

        consistent = True
        if float(list(self.typical_range)[1]) < float(list(self.typical_range)[0]): #satisfying ii
            consistent = False
        
        if len(self.typical_range) != 2: #satisfying i
            consistent = False
        
        return consistent

def inconsistent_typical_range_stations(stations):
    inconsistent_stations_list = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:
            inconsistent_stations_list.append(station)
    return sorted(inconsistent_stations_list)

def test(stations):
    for station in stations:
        return(MonitoringStation.typical_range_consistent(station))
