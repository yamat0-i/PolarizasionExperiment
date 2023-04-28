import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

D1 = np.loadtxt('20230424_5x.txt', delimiter=',',  skiprows=3)
D2 = np.loadtxt('20230424_10x.txt', delimiter=',',  skiprows=3)
D3 = np.loadtxt('20230424_40x.txt', delimiter=',',  skiprows=3)

s1_5x = D1[:,0]
s2_5x = D1[:,1]
s3_5x = D1[:,2]

s1_10x = D2[:,0]
s2_10x = D2[:,1]
s3_10x = D2[:,2]

s1_40x = D3[:,0]
s2_40x = D3[:,1]
s3_40x = D3[:,2]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(s1_5x, s2_5x, s3_5x, marker='.', color='green', label='5x')
ax.scatter(-0.78, 0.55, 0.31, marker='s', s=20,  color='green') # Step10
ax.scatter(-0.77, -0.51, 0.39, marker='v', s=30,  color='green') # Step2

ax.plot(s1_10x, s2_10x, s3_10x, marker='.', color='blue', label='10x')
ax.scatter(-0.76, -0.48, -0.44, marker='s', s=20,  color='blue') # Step10
ax.scatter(-0.66, -0.72, -0.24, marker='v', s=30,  color='blue') # Step2

ax.plot(s1_40x, s2_40x, s3_40x, marker='.',color='red', label='40x')
ax.scatter(-0.59, -0.64, 0.49, marker='s', s=20,  color='red') # Step10
ax.scatter(-0.64, -0.74, -0.23, marker='v', s=30,  color='red') # Step2

ax.set_title('20230424')

ax.set_xlabel('s1')
ax.set_ylabel('s2')
ax.set_zlabel('s3')

ax.legend()

plt.show()