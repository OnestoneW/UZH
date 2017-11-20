import numpy as np
import pylab as plb

values = plb.loadtxt('MLEstim_9_1.dat')
y_points = []
x_points = np.linspace(0, 1, 1000)

for alpha in x_points:
    y_points.append(len(values) * np.log(0.5) + sum(np.log(1 + alpha * values)))

plb.figure()
plb.plot(x_points, y_points)
x_max = x_points[y_points.index(max(y_points))]
lab = "Maximum of log-llh at alpha=" + str(x_points[y_points.index(max(y_points))])
plb.plot(x_max, max(y_points), 'ro', label=lab)
plb.legend()
plb.title("Log-Likelihood of alpha")
plb.xlabel("alpha")
plb.ylabel("log-likelihood function")
plb.show()
