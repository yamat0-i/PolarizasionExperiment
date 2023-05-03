import os

import matplotlib.pyplot as plt

from package.FiberMeasure import measure
from package.Plot3D import Plot3D

main_dir = os.path.dirname(__file__)
date = input("Please enter the date.\n")
data_dir = "{}\\data".format(main_dir)
date_dir = "{}\\{}".format(data_dir, date)

# Analyze
plt.close('all') # Clean Up

FD = measure(main_dir, date, data_dir, date_dir)
FD.measure_diameter()

PE = Plot3D(main_dir, date, data_dir, date_dir)
PE.load_and_plot()
PE.load_and_plot_PS()