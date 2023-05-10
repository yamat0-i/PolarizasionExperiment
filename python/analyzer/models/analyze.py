import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def main():
    date = _input_date()    
    date_dir_path = get_date_dir_path(date)
    load_and_plot(date_dir_path, date)
    load_and_plot_PS(date_dir_path, date)

def _input_date():
    date = input("Please enter the date.\n")
    return date

def _get_DATA_DIR_PATH():
    """Return the path of the data's directory.

    Returns:
        str: The data dir path.
    """
    DATA_DIR_PATH = None

    if not DATA_DIR_PATH:
        MODELS_DIR = Path(os.path.dirname(__file__))
        BASE_DIR = Path(MODELS_DIR.parents[1])
        DATA_DIR_PATH = os.path.join(BASE_DIR, 'data')

    return DATA_DIR_PATH

def get_date_dir_path(date):
    """Return the path of the directory 
        of data for a specific day
        
    Returns:
        str: The 'date' dir path.
    """
    DATA_DIR_PATH = _get_DATA_DIR_PATH()
    date_dir_path = "{}\\{}".format(DATA_DIR_PATH, date)
    return date_dir_path

def load_and_plot(date_dir_path, date):
    """Plot S-parameters in 3D.
    """
    D1 = np.loadtxt(
        '{}\\{}_5x.txt'.format(date_dir_path, date), 
        delimiter=',',  skiprows=3
        )
    D2 = np.loadtxt(
        '{}\\{}_10x.txt'.format(date_dir_path, date), 
        delimiter=',',  skiprows=3
        )
    D3 = np.loadtxt(
        '{}\\{}_40x.txt'.format(date_dir_path, date), 
        delimiter=',',  skiprows=3
        )

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

    ax.set_title('{}(■:step10, ▲:step2)'.format(date))

    ax.set_xlabel('s1')
    ax.set_ylabel('s2')
    ax.set_zlabel('s3')

    ax.legend()

    plt.show()

def load_and_plot_PS(date_dir_path, date):
    """Plot S-parameters on Poincare sphere.
    """
    D1 = np.loadtxt(
        '{}\\{}_5x.txt'.format(date_dir_path, date), 
        delimiter=',',  skiprows=3
        )
    D2 = np.loadtxt(
        '{}\\{}_10x.txt'.format(date_dir_path, date), 
        delimiter=',',  skiprows=3
        )
    D3 = np.loadtxt(
        '{}\\{}_40x.txt'.format(date_dir_path, date), 
        delimiter=',',  skiprows=3
        )
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
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(s1_5x, s2_5x, s3_5x, marker='.', color='green', label='5x')
    ax.scatter(D1[0,0], D1[0,1], D1[0,2], marker='s', s=30,  color='green') # Step10
    ax.scatter(D1[8,0], D1[8,1], D1[8,2], marker='v', s=40,  color='green') # Step2

    ax.plot(s1_10x, s2_10x, s3_10x, marker='.', color='blue', label='10x')
    ax.scatter(D2[0,0], D2[0,1], D2[0,2], marker='s', s=30,  color='blue') # Step10
    ax.scatter(D2[8,0], D2[8,1], D2[8,2], marker='v', s=40,  color='blue') # Step2

    ax.plot(s1_40x, s2_40x, s3_40x, marker='.',color='red', label='40x')
    ax.scatter(D3[0,0], D3[0,1], D3[0,2], marker='s', s=30,  color='red') # Step10
    ax.scatter(D3[8,0], D3[8,1], D3[8,2], marker='v', s=40,  color='red') # Step2


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


    ax.set_title('{}(■:step10, ▲:step2)'.format(date))

    ax.set_xlabel('s1')
    ax.set_ylabel('s2')
    ax.set_zlabel('s3')

    ax.legend()

    plt.show()