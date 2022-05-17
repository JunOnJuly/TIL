import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Grab some test data.
X = np.array([i*0.1 for i in range(-100, 101)])
Y = np.array([i*0.1 for i in range(-100, 101)])
X, Y = np.meshgrid(X, Y)

Z = X**2 + Y**2

X_grad = np.array([i*0.1 for i in range(-100, 101)])
Y_grad = np.array([0 for i in range(-100, 101)])

Z_grad = 10*X_grad - 25

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax.plot(X_grad, Y_grad, Z_grad, 'r')

plt.show()