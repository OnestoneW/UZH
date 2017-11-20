#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab as plb


def read_data(path):
    '''Reads data from txt file and returns an array of form ([line1], [line2]...)'''
    data = plb.loadtxt(path)
    return data


def plot_times(data):
    '''Plots histograms out of a data set'''
    plt.figure()
    times = []
    for line in data:
        times.append(line[2])
    bins = np.linspace(500, 900, 9)

    # the histogram of the data
    n, bins, patches = plt.hist(times, bins, range=(500, 900), facecolor='green', alpha=0.75)

    plt.xlabel('time [min]')
    plt.ylabel('counts')
    plt.title('times of the ironman')
    plt.grid(True)

    plt.show()


def plot_age(data):
    '''Plots histograms out of a data set'''
    plt.figure()
    years = 2010 - data[:, 1]
    bins = np.linspace(10, 90, 11)

    # the histogram of the data
    n, bins, patches = plt.hist(years, bins, range=(10, 90), facecolor='red', alpha=0.75)

    plt.xlabel('age [years]')
    plt.ylabel('counts')
    plt.title('ages of the ironman')
    plt.grid(True)

    plt.show()


def plot_pie(data):
    ages = 2010 - data[:, 1]
    bins_ages = [0, 21, 30, 40, 50, 60, 100]
    n, bins = np.histogram(ages, bins_ages)
    # make a square figure and axes
    plt.figure()
    ax = plt.axes([0.1, 0.1, 0.8, 0.8])

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'under 21', '21 -30', '31-40', '41-50', '51-60', 'over 60'
    fracs = n / len(data[:, 1]) * 100
    plt.pie(fracs, labels=labels,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.title('Participants ironman', bbox={'facecolor': '0.8', 'pad': 5})
    plt.show()


if __name__ == '__main__':
    ironman_path = 'ironman.dat'
    data = read_data(ironman_path)
    plot_times(data)
    plot_age(data)
    plot_pie(data)
