import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

D1 = np.loadtxt('20230426_5x.txt', delimiter=',',  skiprows=3)
D2 = np.loadtxt('20230426_10x.txt', delimiter=',',  skiprows=3)
D3 = np.loadtxt('20230426_40x.txt', delimiter=',',  skiprows=3)

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
ax.scatter(D1[0,0], D1[0,1], D1[0,2], marker='s', s=30,  color='green') # Step10
ax.scatter(D1[8,0], D1[8,1], D1[8,2], marker='v', s=40,  color='green') # Step2

ax.plot(s1_10x, s2_10x, s3_10x, marker='.', color='blue', label='10x')
ax.scatter(D2[0,0], D2[0,1], D2[0,2], marker='s', s=30,  color='blue') # Step10
ax.scatter(D2[8,0], D2[8,1], D2[8,2], marker='v', s=40,  color='blue') # Step2

ax.plot(s1_40x, s2_40x, s3_40x, marker='.',color='red', label='40x')
ax.scatter(D3[0,0], D3[0,1], D3[0,2], marker='s', s=30,  color='red') # Step10
ax.scatter(D3[8,0], D3[8,1], D3[8,2], marker='v', s=40,  color='red') # Step2

ax.set_title('20230426(■:step10, ▲:step2)')

ax.set_xlabel('s1')
ax.set_ylabel('s2')
ax.set_zlabel('s3')

ax.legend()

plt.show()