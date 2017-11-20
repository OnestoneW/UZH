import numpy as np
import pylab as plb
import scipy.stats as sp

def factorial(n):
    '''Calculates the factorial of a number'''
    if n <= 1:
        return 1
    return n*factorial(n-1)

def binomial_dist(k, p, n):
    prop = (factorial(n)/(factorial(k)*factorial(n-k)))*(p**k)*(1-p)**(n-k)
    expected_value = n*p
    std_deviation = np.sqrt(n*p*(1-p))
    return prop, expected_value, std_deviation

def gaussion_dist(mu, sigma, x):
    return (1/(np.sqrt(2*np.pi*sigma**2)))*(1/(np.e**((x-mu)**2)/(2*sigma**2)))

if __name__ == "__main__":
    decay = 0.8
    k = 340
    n = 400
    mu = n * decay
    sigma = np.sqrt(n * decay * (1 - decay))
    #propability, expected_value, std_deviation = binomial_dist(k, decay, n)
    propability = sp.binom(n, decay).pmf(k)
    print("Propability for 340 detections in 400 Z-Bosons:", round(propability*100, 3), "%")
    gauss = sp.norm(mu, sigma).pdf(k)

    print("Propability for 340 detections in 400 Z-Bosons as gaussian dist:", round(100*gauss, 3), "%")
    plb.figure()
    plb.plot(k, 100*propability, 'bx', label='binomial')
    plb.plot(k, 100*gauss, 'r.', label='gaussian')
    plb.legend()
    plb.title("Binomial vs. Gaussian distribution")
    plb.ylabel("Propability in [%]")
    plb.xlabel("Number of detected charched particles")
    plb.grid()
    x = plb.frange(0, 400, 20)
    y_binomial = []
    y_gauss = []
    for nr in x:
        y_gauss.append(sp.norm(mu, sigma).pdf(nr))
        y_binomial.append(sp.binom(n, decay).pmf(nr))

    f, axxarr = plb.subplots(2)
    plb.title("Binomial vs. Gaussian dist.")
    axxarr[0].plot(x, y_gauss, 'g')
    plb.xlabel("Number of detected particles")
    plb.ylabel("Propability")

    axxarr[1].plot(x, y_binomial)

    plb.show()
