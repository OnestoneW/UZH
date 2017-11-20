import random as rand
import numpy as np
import pylab as plb
import scipy.stats as sp

numbers = plb.rand(10**4)
def a():
    bins = np.linspace(0, 1, len(numbers)/10)
    plb.figure()
    plb.hist(numbers, bins=bins)
    plb.ylabel("Number of events")
    plb.xlabel("random number")
    plb.title("Uniform distribution")
    plb.figure()
    new_bins = np.linspace(0, 1, 50)
    plb.title("Uniform distribution")
    plb.ylabel("Number of events")
    plb.xlabel("random number")
    plb.hist(numbers, bins=new_bins)
    plb.show()

def b():
    bins = np.linspace(0, 1, len(numbers) / 10)
    n, bins, patches = plb.hist(numbers, bins=bins)
    plb.figure()
    plb.hist(n)
    x = np.linspace(0, 20, len(n))
    variance = np.mean(n**2) - np.mean(n)**2
    mean_value = np.mean(n)
    print("Observed mean value:", mean_value)
    print("Observed std deviation:", np.sqrt(variance))
    print("Pretty close to the calculated values.")
    a = 2000
    plb.plot(x, a*sp.norm.pdf(x, loc=10, scale=np.sqrt(variance)))
    plb.title("Plot of events per bin")
    plb.xlabel("distribution of events per bin")
    plb.ylabel("Events per bin")
    plb.show()

if __name__ == "__main__":

    b()
'''
a)
The expected shape of those are rectangles since the values are uniformly distributed. The thinner the bins are,
the more disortion is in the shape. The mean value is 1/2*(a+b) = 1/2. The std. deviation is 1/sqrt(12)*(b-a) = 1/sqrt(12)

b)

'''