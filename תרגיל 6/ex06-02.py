import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

coords = np.genfromtxt('data06-02.txt', delimiter=',')

fig = plt.figure()

x, y = coords[:, 0], coords[:, 1]

graph1 = fig.add_subplot(211)
graph1.plot(x, y, 'o')

interpolation = interpolate.interp1d(x, y, bounds_error=False, fill_value=min(y))
new_x = np.arange(min(x), max(x), 0.1)
new_y = interpolation(new_x)

graph2 = fig.add_subplot(212)
graph2.plot(x, y, 'o', new_x, new_y, '-')

plt.show()