import matplotlib.pyplot as plt
from matplotlib import pylab as plb


def read_data(path):
    '''Reads data from txt file and returns an array of form ([line1], [line2]...)'''
    data = plb.loadtxt(path)
    return data

def scatter_plot(x_values, y_values, title):
    plt.figure()
    plt.plot(x_values, y_values, 'r.')
    plt.title(title)
    plt.show()

if __name__ == '__main__':

    #Get data from the .dat file and order it:
    data = read_data('ironman.dat')
    total_rank = data[:, 0]
    age = 2010 - data[:, 1]
    total_time = data[:, 2]
    swimming_time = data[:, 3]
    swimming_rank = data[:, 4]
    cycling_time = data[:, 5]
    cycling_rank = data[:, 6]
    running_time = data[:, 7]
    running_rank = data[:, 8]

    #Plot those data sets:
    scatter_plot(total_time, total_rank, "total time versus total rank")
    scatter_plot(total_time, age, "total time versus age")
    scatter_plot(running_time, swimming_time, "running time versus swimming time")
    scatter_plot(total_time, swimming_time, "total time versus swimming time")
    scatter_plot(total_time, cycling_time, "cycling time versus total time")
    scatter_plot(total_time, running_time, "running time versus total time")

    '''Answer to the question:
    
    I see and expected, that the ones with the lower total time have also a low time at the single disciplines.
    Also I expected that the elder participants have a much higher total time than the younger ones. We can
    see that in the data too, but I thought the difference would be much bigger.
    '''
