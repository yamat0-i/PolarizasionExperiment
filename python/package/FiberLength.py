import numpy as np
import matplotlib.pyplot as plt


class measure_length(object):
    def __init__(self, date):
        self.date = date

    def measure(self):
        D = np.loadtxt('data\\{}\\FiberLength_{}.txt'.format(self.date, self.date), delimiter=',',  skiprows=3)

        X = D[:,0]
        y1 = D[:,1]
        y2 = D[:,2]

        diameter = y2 - y1

        diameter_min = np.nanmin(diameter)
        diameter_min_index = np.argmin(diameter)
        X_min = X[diameter_min_index]
        print('X:', X_min, ',', 'diameter:', diameter_min)

        plt.figure()
        plt.plot(X, diameter)

        plt.xlabel('X absolute position')
        plt.ylabel('diameter[px]')
        plt.title('{}_FiberDiameter'.format(self.date))

        plt.show()