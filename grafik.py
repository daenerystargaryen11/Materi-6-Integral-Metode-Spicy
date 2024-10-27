import numpy as np
from spicy import integrate
import matplotlib.pyplot as plt

x_start = 0
x_stop = np.pi
x_steps_interval = 0.01

x_values = np.arange(x_start, x_stop, x_steps_interval)
y_values = x_values **2 * np.cos(x_values) + 3 * np.sin(2*x_values)

plt.plot(x_values, y_values, label=r'$f(x) = x^2 \cos(x) + 3 \sin(2x)$', color='blue')
plt.fill_between(x_values, y_values, color='skyblue', alpha=0.4)

integration_function = lambda x:x**2 * np.cos(x) + 3 * np.sin(2*x)
integral, _ = integrate.quad(integration_function, x_start, x_stop)

print("Nilai Integral:", integral)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik Fungsi $e^{-x^2}$ dan Area di Bawah Kurva')
plt.legend()
plt.show()
