from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

X = np.array([[0, 1, 2]])

X_new = np.array([])
for i in range(len(X)):
    X_new[i] = X