import numpy as np
import matplotlib.pyplot as plt

D = np.loadtxt('20230426\\20230426_10x.txt', delimiter=',',  skiprows=2)

s1 = D[:,0]
s2 = D[:,1]
s3 = D[:,2]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(s1, s2, s3, color='blue', label='label')

ax.set_title('10x')

ax.set_xlabel('s1')
ax.set_ylabel('s2')
ax.set_zlabel('s3')

ax.legend()

plt.show()