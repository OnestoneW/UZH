import pylab as plb
import numpy as np
import matplotlib

def calc_average_radiation(data_set):
    values = data_set[:,0]
    errors = data_set[:,1]

    #calc the measurements for "per year":
    values = values*365*24
    errors = errors*365*24

    weights = 1/(errors**2)

    average = sum((weights*values))/sum(weights)

    error_on_average = (1/np.sqrt(sum(weights)))/np.sqrt(len(weights))

    return average, error_on_average


if __name__ == "__main__":
    data = plb.loadtxt("radiation.dat")
    average, error = calc_average_radiation(data)
    result = "({} +/- {}) mSv/year".format(round(average, 3), round(error, 3))
    print("Average radiation per year:",result)

    '''Taking a look onto the natural radiation of 2.4 mSv/year, our result is about (0.191 +/- 0.012) mSv/year higher.
        Since this is only about 8% higher as the natural background radiation, it is compatible.'''