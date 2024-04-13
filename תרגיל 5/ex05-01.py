import matplotlib.pyplot as plt
import numpy as np

# load coordinates from file
coords = np.genfromtxt('data05-01.txt', delimiter=',')

fig = plt.figure()

graph1 = fig.add_subplot(211)
graph1.plot(coords[:, 0], coords[:, 1], 'b.')

graph2 = fig.add_subplot(212)
graph2.plot(coords[5:, 0], coords[5:, 1], 'r.-')

plt.show()