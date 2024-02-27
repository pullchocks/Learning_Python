import numpy as np
import matplotlib.pyplot as plt

plt.get_current_fig_manager().set_window_title('Scatter Project')

x = np.arange(24)
y = np.random.randint(0, 401, size=x.shape)

degree = 3
coeffs = np.polyfit(x, y, degree)
poly = np.poly1d(coeffs)

x_curve = np.linspace(x.min(), x.max(), 500)
y_curve = poly(x_curve)

plt.scatter(x, y, color='blue', label='Visitors')
plt.plot(x_curve, y_curve, color='red', label='Trend Line')
plt.xlabel('Hour')
plt.ylabel('Visitors')
plt.title('Visitors per Hour Average')
plt.legend()

plt.xlim(left=0)
plt.ylim(bottom=0)

plt.show()
