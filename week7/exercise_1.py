import scipy.stats as sp
import numpy as np
import pylab as plb



if __name__ == "__main__":
    first = sp.cauchy(50, 5).rvs(size=10000)
    second =  sp.cauchy(80, 5).rvs(size=10000)
    dist = np.concatenate((first, second))
    bins = np.linspace(-100, 200, 100)
    plb.figure()
    plb.xlabel("number")
    plb.ylabel("count")
    plb.title("Two cauchy distributions")
    plb.hist(dist, bins=bins)
    plb.show()
    gauss_1 = sp.norm.pdf(dist, loc=0, scale=5)
    gauss_2 = sp.norm.pdf(dist, loc=0, scale=10)
    gauss_3 = sp.norm.pdf(dist, loc=0, scale=15)
    plb.figure()
    plb.hist(gauss_1, bins=np.linspace(min(gauss_1), max(gauss_1), 100))
    plb.show()