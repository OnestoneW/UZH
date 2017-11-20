import scipy.stats as sp
import scipy.misc as msc
import numpy as np
import pylab as plb

def create_decay(t, tau):
    return (1/tau) * np.exp(-(t/tau))


def log_likelihood(n, bns, a):
    n = list(n)
    all_n = sum(n)
    bns = list(bns)[:-1]
    my_sum = 0
    for element in bns:
        n_i = n[bns.index(element)]
        v_i = all_n*create_decay(element, a)
        my_sum += np.absolute(n_i*np.log(v_i)-v_i)


    return my_sum


if __name__ == "__main__":
    tau = 6.5
    times = sp.expon(0, tau).rvs(1000)
    x = plb.frange(0, 20, 1)
    centers = x+0.5

    my_pi = []
    plb.figure()
    number_of_entry, bins_of_hist, patches = plb.hist(times, bins=x)
    plb.xlabel("times")
    plb.title("1000 decay times")
    plb.ylabel("entry per bin")
    estimator = (1/len(times))*sum(times)
    print("Calculated estimator:", estimator)
    x_values = np.linspace(5, 9, 1000)
    y_values = []
    for a in x_values:
        y_values.append(log_likelihood(number_of_entry, bins_of_hist, a))

    maximum = x_values[y_values.index(max(y_values))]
    print("Maximum of log-likelihood:", maximum)
    plb.figure()
    plb.plot(x_values, y_values)
    plb.plot(maximum, max(y_values), 'ro', label="Maximum")
    plb.xlabel("estimated tau")
    plb.ylabel("log-likelihood")
    plb.legend()
    plb.title("log-likelihood")
    plb.show()
    '''The two extimators are really close to each other. In most cases the estimator from log-likelihood is slightly bigger.'''

