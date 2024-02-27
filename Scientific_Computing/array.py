import numpy as np


oneD = np.array([1, 2, 3, 4])
twoD = np.array([[1, 2, 3], [3, 3, 3], [-1, -0.5, 4], [0, 1, 0]])


print("For oneD array:")
print("Minimum value:", oneD.min())
print("Maximum value:", oneD.max())
print("Mean value:", oneD.mean())
print("Median value:", np.median(oneD))
print()

print("For twoD array:")
print("Minimum value:", twoD.min())
print("Maximum value:", twoD.max())
print("Mean value:", twoD.mean())
print("Median value:", np.median(twoD))