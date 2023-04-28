import numpy as np
import matplotlib.pyplot as plt


class Plot3D(object):
    def __init__(self, fname):
        self.fname = fname

    def load_and_plot(self, fignumber):
        D = np.loadtxt('{}'.format(self.fname), delimiter=',',  skiprows=3)
        s1 = D[:,0]
        s2 = D[:,1]
        s3 = D[:,2]
        
        self.fignumber = fignumber
        fig = plt.figure(self.fignumber)
        ax = fig.add_subplot(projection='3d')
        ax.plot(s1, s2, s3, marker='.', color='green', label='5x')
        ax.scatter(D[0,0], D[0,1], D[0,2], marker='s', s=30,  color='green') # Step10
        ax.scatter(D[8, 0], D[8, 1], D[8, 2], marker='v', s=40,  color='green') # Step2

        ax.set_title(self.fname)

        ax.set_xlabel('s1')
        ax.set_ylabel('s2')
        ax.set_zlabel('s3')

        ax.legend()

        plt.show()