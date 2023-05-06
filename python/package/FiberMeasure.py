import numpy as np
import matplotlib.pyplot as plt


class measure(object):
    def __init__(self, MAIN_DIR, date, DATA_DIR, date_dir):
        self.MAIN_DIR = MAIN_DIR
        self.date = date
        self.DATA_DIR = DATA_DIR
        self.date_dir = date_dir

    def measure_diameter(self):
        """Examine the thinnest part of fiber.

        X: Absolute position
        y1: Upper edge of fiber
        y2: Lower edge of fiber
        """

        D = np.loadtxt(
            '{}\\FiberDiameter_{}.txt'.format(self.date_dir, self.date), 
            delimiter=',',  skiprows=3
            )

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
        plt.title('FiberDiameter_{}'.format(self.date))

        plt.show()