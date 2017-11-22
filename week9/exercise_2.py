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

    mu_x = np.linspace(3, 7, 50)
    sigma_x = np.linspace(0.5, 3, 50)
    likelihood_matrix = np.zeros((mu_x.size, sigma_x.size))
    for mu in range(len(mu_x)):
        for sigma in range(len(sigma_x)):
            likelihood_matrix[mu, sigma] = np.exp(-1/2*20*np.log(2*np.pi*sigma_x[sigma]**2)-sum((gaussian_events-mu_x[mu])**2/(2*sigma_x[sigma]**2)))

    plb.figure()
    X, Y = plb.meshgrid(mu_x, sigma_x)
    plb.contour(X, Y, likelihood_matrix.T)
    plb.xlabel("mu")
    plb.ylabel("sigma")
    plb.title("Countour Plot of estimators")
    max_value = np.max(likelihood_matrix)
    local_max_index = np.where(likelihood_matrix == max_value)
    max_x = X[local_max_index[0], local_max_index[1]]
    max_y = Y[local_max_index[0], local_max_index[1]]
    plb.plot(max_x, max_y, marker='o')
    print('the max value will be reached at mu: ', max_x, ' and sigma: ', max_y)
    plb.show()

    # Exercise 2, 6.:
    x_maximum_values = []
    y_maximum_values = []
    for i in range(1000):
        print(i, "processed")
        gaussian_sample = sp.norm(loc=5, scale=2).rvs(20)
        likelihood_matrix = np.zeros((mu_x.size, sigma_x.size))
        for mu in range(len(mu_x)):
            for sigma in range(len(sigma_x)):
                likelihood_matrix[mu, sigma] = np.exp(-1 / 2 * 20 * np.log(2 * np.pi * sigma_x[sigma] ** 2) - sum(
                    (gaussian_events - mu_x[mu]) ** 2 / (2 * sigma_x[sigma] ** 2)))
        max_value = np.max(likelihood_matrix)
        local_max_index = np.where(likelihood_matrix == max_value)
        max_x = float(X[local_max_index[0], local_max_index[1]])
        max_y = float(Y[local_max_index[0], local_max_index[1]])
        x_maximum_values.append(max_x)
        y_maximum_values.append(max_y)

    print("Start histogram")
    print(x_maximum_values)
    plb.figure()
    plb.hist(x_maximum_values, bins=np.linspace(min(x_maximum_values), max(x_maximum_values), 30), histtype='step')
    plb.hist(y_maximum_values, bins=np.linspace(min(y_maximum_values), max(y_maximum_values), 30), histtype='step')
    plb.show()