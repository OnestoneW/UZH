'''
Gaussian distributed x_n
1. calculate the max-llh estimators for mu and sigma
2. calculate the covariance matrix for estimators mu and sigma
3. compute expected uncercainity on estimators mu and sigma when est_sigma = 2 and n = 20
unsicherheit auf schätzwert = sqrt(-1/zweiteableitung(L(a)))
'''
import numpy as np
import pylab as plb
import scipy.stats as sp

def mu_estimator(x):
    return (1/len(x))*sum(x)

def sigma_estimator_squared(x, mu_est):
    return (1/len(x)) * sum((x-mu_est)**2)

def covariance_matrix(mu_est, sigma_est, x):
    return np.array([(sigma_est**2)/len(x), 0], [0, (2*sigma_est**2)/len(x)])

if __name__ == "__main__":
    mu_range = np.linspace(4.7, 5.3, 1000)
    x = sp.norm(loc=0, scale=2).rvs(1000)
    y_values = []
    for mu in mu_range:
        y_values.append(mu_estimator(x))
    plb.figure()
    plb.plot(mu_range, y_values)
    plb.show()