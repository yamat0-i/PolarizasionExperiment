import numpy as np
import matplotlib.pyplot as plt

from package.Plot3D import Plot3D

#Clean Up
plt.close('all')

PE20220426_5x = Plot3D("20230426/20230426_5x.txt")
PE20220426_10x = Plot3D("20230426/20230426_10x.txt")
PE20220426_40x = Plot3D("20230426/20230426_40x.txt")

PE20220426_5x.load_and_plot(1)
PE20220426_10x.load_and_plot(1)
PE20220426_40x.load_and_plot(1)