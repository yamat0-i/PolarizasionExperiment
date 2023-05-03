import os

import matplotlib.pyplot as plt

from package.FiberMeasure import measure
from package.Plot3D import Plot3D


main_dir = os.path.dirname(__file__)

# Analyze
plt.close('all') # Clean Up

date = input("Please enter the date.\n")

FD = measure(date, main_dir)
FD.measure_diameter()

PE = Plot3D(date, main_dir)
PE.load_and_plot()
PE.load_and_plot_PS()