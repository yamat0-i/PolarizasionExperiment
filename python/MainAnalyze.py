"""
This script is intended for the analysis of polarization control experiments.

Please run in the 'python' directory where this file exists.
"""

import os

import matplotlib.pyplot as plt

from package.FiberMeasure import measure
from package.Plot3D import Plot3D

#Check CD


#Clean Up
plt.close('all')

PE20230501 = Plot3D("20230501")
PE20230501.load_and_plot(1)
PE20230501.load_and_plot_PS(2)

FL20230502 = measure("20230502")
FL20230502.measure_diameter()


# PE20230424 = Plot3D("20230424")
# PE20230424.load_and_plot(1)
# PE20230424.load_and_plot_PS(2)

# PE20230425 = Plot3D("20230425")
# PE20230425.load_and_plot(3)
# PE20230425.load_and_plot_PS(4)

# PE20230426 = Plot3D("20230426")
# PE20230426.load_and_plot(5)
# PE20230426.load_and_plot_PS(6)