import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

def main():
    date = _input_date()    
    date_dir_path = get_date_dir_path(date)
    measure_diameter(date_dir_path, date)

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

def measure_diameter(date_dir_path, date):
        """Examine the thinnest part of fiber.

        X: Absolute position
        y1: Upper edge of fiber
        y2: Lower edge of fiber
        """

        D = np.loadtxt(
            '{}\\FiberDiameter_{}.txt'.format(date_dir_path, date), 
            delimiter=',',  skiprows=3
            )

        X = D[:,0]
        y1 = D[:,1]
        y2 = D[:,2]

        diameter = y2 - y1

        diameter_min = np.nanmin(diameter)
        diameter_min_index = np.argmin(diameter)
        X_min = X[diameter_min_index]
        print('X:', X_min, ',', 'diameter:', diameter_min)

        plt.figure()
        plt.plot(X, diameter)

        plt.xlabel('X absolute position')
        plt.ylabel('diameter[px]')
        plt.title('FiberDiameter_{}'.format(date))

        plt.show()