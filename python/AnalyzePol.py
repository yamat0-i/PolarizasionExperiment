import matplotlib.pyplot as plt

from package.Plot3D import Plot3D

#Clean Up
plt.close('all')

PE20230424 = Plot3D("20230424")
PE20230424.load_and_plot(1)
PE20230424.load_and_plot_PS(2)

PE20230425 = Plot3D("20230425")
PE20230425.load_and_plot(3)
PE20230425.load_and_plot_PS(4)

PE20230426 = Plot3D("20230426")
PE20230426.load_and_plot(5)
PE20230426.load_and_plot_PS(6)