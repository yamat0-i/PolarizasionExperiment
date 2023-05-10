import numpy as np
import matplotlib.pyplot as plt

def Plot_PS():
    """Plot S-parameters on Poincare sphere.
    """
    date = 20230509

    H = [0.94, -0.10, -0.32]
    I = [0.45, -0.84, 0.29]

    L1 = [0.37, -0.81, 0.45]
    L2 = [-0.48, -0.66, -0.58]
    array_L = np.array([L1, L2])

    R1 = [-0.52, 0.78, -0.35]
    R2 = [0.49, 0.65, 0.58]
    array_R = np.array([R1, R2])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(H[0], H[1], H[2], marker='o', s = 40, color='red', label='H')
    ax.scatter(I[0], I[1], I[2], marker='o', s = 40, color='blue', label='I')

    ax.plot(array_L[:,0], array_L[:,1], array_L[:, 2], marker = '.', color = 'green')
    ax.scatter(L1[0], L1[1], L1[2], marker='s', s = 30, color='green', label='L1')
    ax.scatter(L2[0], L2[1], L2[2], marker='v', s = 40, color='green', label='L2')

    ax.plot(array_R[:,0], array_R[:,1], array_R[:, 2], marker = '.', color = 'orange')
    ax.scatter(R1[0], R1[1], R1[2], marker='s', s = 30, color='orange', label='R1')
    ax.scatter(R2[0], R2[1], R2[2], marker='v', s = 40, color='orange', label='R2')


    # Poincare sphere
    r = 1
    theta_1_0 = np.linspace(0, 2*np.pi, 400)
    theta_2_0 = np.linspace(0, 2*np.pi, 400)
    theta_1, theta_2 = np.meshgrid(theta_1_0, theta_2_0)
    x = np.cos(theta_2)*np.sin(theta_1) * r
    y = np.sin(theta_2)*np.sin(theta_1) * r
    z = np.cos(theta_1) * r

    ax.plot_wireframe(x,y,z, color='lightskyblue', linewidth=0.5)
    plt.xlim([-1,1])
    plt.ylim([1,-1])
    ax.set_zlim([-1,1])
    ax.set_aspect('equal')


    ax.set_title('{}(Waveplate ■:1, ▲:2)'.format(date))

    ax.set_xlabel('s1')
    ax.set_ylabel('s2')
    ax.set_zlabel('s3')

    ax.legend()

    plt.show()

Plot_PS()