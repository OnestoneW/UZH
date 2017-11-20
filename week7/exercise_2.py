import pylab as plb
import scipy.stats as sp
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

'''
I know I should have used 2d arrays for my x and y axis. But I couldn`t figure out how...
Therefore also the surface plot and the contour does not make any sense.
'''

if __name__ == "__main__":
    mean_x = 2
    mean_y = 5
    sigma_x = 0.8
    sigma_y = 1.2
    coefficient = -0.7
    cov = plb.array([[sigma_x**2, sigma_x*sigma_y*coefficient], [sigma_x*sigma_y*coefficient, sigma_y**2]])
    x, y = np.random.multivariate_normal(plb.array([mean_x, mean_y]), cov, 2000).T
    calculated_mu_x = np.mean(x)
    calculated_mu_y = np.mean(y)
    calculated_std_x = np.mean(x**2) - np.mean(x)**2
    calculated_std_y = np.mean(y**2) - np.mean(y)**2
    print(calculated_mu_x, calculated_mu_y, calculated_std_x, calculated_std_y)
    plb.plot(x, y, "x")
    plb.axis("equal")
    plb.title("2-D gaussian")
    plb.xlabel("first gaussian")
    plb.ylabel("second gaussian")
    plb.show()
    x_new, y_new = np.random.multivariate_normal(plb.array([mean_x, mean_y]), cov, 100000).T
    calculated_mu_x = np.mean(x_new)
    calculated_mu_y = np.mean(y_new)
    calculated_std_x = np.mean(x_new ** 2) - np.mean(x_new) ** 2
    calculated_std_y = np.mean(y_new ** 2) - np.mean(y_new) ** 2
    print(calculated_mu_x, calculated_mu_y, calculated_std_x, calculated_std_y)
    z, x_bins, y_bins = np.histogram2d(x_new, y_new, bins=200)
    x_plot = x_bins*len(x_bins)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_wireframe(x_bins[:-1], y_bins[:-1], z, rstride=10, cstride=10)

    plt.show()

