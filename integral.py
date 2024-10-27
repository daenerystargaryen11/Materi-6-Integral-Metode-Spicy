import numpy as np
from spicy import integrate
import matplotlib.pyplot as plotlib

#define parameters
x_start = 0 #start of the interval
x_stop = np.pi # end of the interval
x_steps_interval = 0.01 #step size

#define an array of data points
x_values = np.arange(x_start, x_stop, x_steps_interval)
y_values = x_values **2 * np.cos(x_values) + 3 * np.sin(2*x_values)

# plot the function curve
plotlib.plot(x_values, y_values)

# define a lambda function for integration
integration_function = lambda x: x**2 * np.cos(x) + 3 * np.sin(2*x)

# calculate the integral(ignoring error)
integral, _ = integrate.quad(integration_function, x_start, x_stop)

# print the integration result
print("Integral Values:")
print(integral)

#display the plot
plotlib.xlabel('x')
plotlib.ylabel('f(x)')
plotlib.title('plot of f(x) = x**2 * np.cos(x) + 3 * np.sin(2*x)' )
plotlib.show
