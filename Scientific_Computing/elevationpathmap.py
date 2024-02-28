import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v0 = 10
angle = np.pi / 4
g = 9.81

t_total = 2 * v0 * np.sin(angle) / g

time = np.linspace(0, t_total, 100)

x = v0 * np.cos(angle) * time
y = np.zeros_like(time)
z = v0 * np.sin(angle) * time - 0.5 * g * time**2

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)

X, Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))

ax.plot_surface(X, Y, np.zeros_like(X), alpha=0.5, color='gray')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()