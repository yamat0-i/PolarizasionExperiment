import numpy as np
import matplotlib.pyplot as plt

D = np.loadtxt('data\\{}\\FiberLength_{}'.format(self.date, self.date), delimiter=',',  skiprows=1)

x = D[:,0]
y1 = D[:.1]
y2 = D[:,2]

y = y2 - y1

plt.figure()
plt.plot(x, y)