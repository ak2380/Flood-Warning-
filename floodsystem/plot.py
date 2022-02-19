import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):

    high = station.typical_range[1]
    low = station.typical_range[0]

    # Plot
    plt.plot(dates, levels)
    plt.hlines(y=high, xmin=dates[0], xmax=dates[-1],color='red')
    plt.hlines(y=low, xmin=dates[0], xmax=dates[-1],color='gold')


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station Name:{}".format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()



def plot_water_level_with_fit(station, dates, levels, p):
    # station is a MonitoringStation object
    # Plots the water level data with the best-fit polynomial
    poly, shift = polyfit(dates, levels, p)

    # Plot original data points
    plt.plot(dates, levels, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial is evaluated using the shift x)
    x = matplotlib.dates.date2num(dates)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - shift))

    # Plot max and min ranges
    plt.plot([min(dates),max(dates)], [station.typical_range[0], station.typical_range[0]])
    plt.plot([min(dates),max(dates)], [station.typical_range[1], station.typical_range[1]])

    plt.xlabel('Date/time since %s' % dates[0])
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation = 45)
    plt.title("{}".format(station.name))

    # Display plot
    plt.tight_layout()
    plt.show()