import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

def polyfit(dates, levels, p):
    # given the water level time history (dates, levels) for a station computes a least-squares fit of a polynomial of degree p to water level data. 
    # The function should return a tuple of (i) the polynomial object and (ii) any shift of the time (date) axis
   
    x = matplotlib.dates.date2num(dates)
    y = levels
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    shift = x[0]
    p_coeff = np.polyfit(x - shift, y, p)
    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return (poly, shift)

