import numpy as np
import scipy.stats as sp
import pylab as plb
import math

def hit_and_miss():
    x = list(sp.uniform.rvs(loc=0, scale=4, size=1000))
    y = list(sp.uniform.rvs(loc=0, scale=0.5, size=1000))
    x_accepted = []
    for number in x:
        if y[x.index(number)] <= sp.norm.pdf(number, loc=2, scale=5):
            x_accepted.append(number)
    return x_accepted

def invert_cdf():
    uniform = sp.uniform.rvs(loc=0, scale=4, size=1000)
    ran = sp.norm.ppf(uniform, loc=2, scale=5)
    gauss = []
    for number in ran:
        if not math.isnan(number):
            gauss.append(number)
    plb.figure()
    bins = np.linspace(0, 4, 20)
    plb.hist(gauss, bins=bins)
    plb.show()

if __name__ == "__main__":
    x = hit_and_miss()
    print(len(x))
    bins = np.linspace(0, 4, 100)
    plb.figure()
    plb.hist(x, bins=bins)
    plb.show()
    invert_cdf()