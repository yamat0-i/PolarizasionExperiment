import matplotlib.pyplot as plt

from package.Plot3D import Plot3D

#Clean Up
plt.close('all')

PE20230426 = Plot3D("20230426")
PE20230426.load_and_plot(1)
PE20230426.load_and_plot_PS(2)