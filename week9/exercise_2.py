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

def covariance_matrix(sigma_est, x):
    return np.array([(sigma_est**2)/len(x), 0], [0, (2*sigma_est**2)/len(x)])

def likelihood_of_gaussian(mu, sigma, x):
    return ((2*np.pi*sigma**2)**(-len(x)/2))*np.exp(-(1/(2*sigma**2))*sum((x-mu)**2))

if __name__ == "__main__":
    gaussian_events = sp.norm(loc=5, scale=2).rvs(20)
    #bins = np.linspace(min(gaussian_events), max(gaussian_events), 8)

    mu_x = np.linspace(3, 7, 500)
    sigma_x = np.linspace(0.5, 3, 500)
    mu_values = []
    sigma_values = []
    for mu in mu_x:
        for sigma in sigma_x:
            mu_values.append(likelihood_of_gaussian(mu, sigma, gaussian_events))

    for sigma in sigma_x:
        for mu in mu_x:
            sigma_values.append(likelihood_of_gaussian(mu, sigma, gaussian_events))
    plb.figure()
    plb.plot(np.linspace(min(mu_values), max(mu_values), len(mu_values)), mu_values, 'b', label="mu estimation")
    plb.figure()
    plb.plot(np.linspace(min(sigma_values), max(sigma_values), len(sigma_values)), sigma_values, 'r', label="sigma estimation")
    plb.legend()
    print("likelihood has maximum at mu=", np.linspace(min(mu_values), max(mu_values), len(mu_values))[mu_values.index(max(mu_values))])
    print("likelihood has maximum at sigma=", np.linspace(min(sigma_values), max(sigma_values), len(sigma_values))[sigma_values.index(max(sigma_values))])
    plb.show()


    '''
    plb.figure()
    plb.hist(gaussian_events, bins=bins)
    plb.show()
    '''