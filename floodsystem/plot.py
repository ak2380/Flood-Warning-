import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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