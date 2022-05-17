import matplotlib.pyplot as plt
import numpy as np


X = np.arange(-10, 10, 0.1)
Y = X**2

gradient_x = np.array([0, 10])
gradient_y = gradient_x*10 - 25

plt.plot(gradient_x, gradient_y, 'r')
plt.plot(X, Y)
plt.show()