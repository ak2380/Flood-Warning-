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

    def typical_range_consistent(self): #Task 1F a
        if self.typical_range != None:
            lower = float(self.typical_range[0])
            upper = float(self.typical_range[1])
            if lower <= upper:
                return True
        return False

    def relative_water_level(self):
        try:
            return (self.latest_level - self.typcial_range[0])/(self.typcial_range[1]-self.typcial_range[0])
        except:
            return None


def inconsistent_typical_range_stations(stations): #Task 1F b
    inconsistent_stations_list = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_stations_list.append(station.name)
    return sorted(inconsistent_stations_list)
