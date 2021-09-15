import math
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn
import numpy as np

# Helper functions


def create_histograms(data, lower_bound=-1, upper_bound=-1, n_bins=5):
    """
    Create histogram bins for given data points
    :param data: a python list of data points expected to be in int or float or mixture
    :param lower_bound: define a lower bound to draw histogram
    :param upper_bound: define an upper bound to draw histogram
    :param n_bins: number of classes
    :return: dictionary of data points placed in n_bins of bins
    """
    # If data is an empty list
    if not data:
        return {"0": data}

    # Sort data points
    data.sort()
    if lower_bound == -1:
        min_ = data[0]
    else:
        min_ = lower_bound
    if upper_bound == -1:
        max_ = data[-1]
    else:
        max_ = upper_bound

    histogram_dict = dict()

    bin_width = math.ceil((max_-min_+1)/n_bins)
    intervals = list(range(min_, max_+bin_width, bin_width))

    for ix, _ in enumerate(intervals[:-1]):
        # get data points in given interval
        histogram_dict[(intervals[ix], intervals[ix+1]-1)] = [x for x in data if intervals[ix] <= x < intervals[ix+1]]

    # draw
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    xs = [str(x[0])+'-'+str(x[1]) for x in list(histogram_dict.keys())]
    ys = [len(x) for x in histogram_dict.values()]
    ax.bar(xs, ys)
    plt.show()
    return histogram_dict
