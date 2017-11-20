import numpy as np
import pylab as plb
import scipy.stats as sp

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

def binomial(n, k, p):
    '''
    :param n: how many repetitions
    :param k: positive cases
    :param p: propability
    :return:
    '''
    binomial_coefficient = factorial(n)/(factorial(k)*factorial(n-k))
    propability = binomial_coefficient * (p**k) * (1-p)**(n-k)
    return propability

if __name__ == "__main__":
    prop = binomial(1, 1, 0.5)
    print(prop)