import os

import matplotlib.pyplot as plt

from package.FiberMeasure import measure
from package.Plot3D import Plot3D

MAIN_DIR = os.path.dirname(__file__)
date = input("Please enter the date.\n")
DATA_DIR = "{}\\data".format(MAIN_DIR)
date_dir = "{}\\{}".format(DATA_DIR, date)

# Analyze
plt.close('all') # Clean Up

FD = measure(MAIN_DIR, date, DATA_DIR, date_dir)
FD.measure_diameter()

PE = Plot3D(MAIN_DIR, date, DATA_DIR, date_dir)
PE.load_and_plot()
PE.load_and_plot_PS()