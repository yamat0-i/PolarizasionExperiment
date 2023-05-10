import os
from pathlib import Path

from analyzer.views import console

def main():
    date = _input_date()    
    DATE_DIR_PATH = get_DATE_DIR_PATH(date)
    is_DATE_DIR_existed(date_dir_path=DATE_DIR_PATH)
    create_files(
        fname="{}\\FiberDiameter_{}.txt".format(DATE_DIR_PATH, date),
        temp_file='diameter.txt',
        lensX=''
        )
    create_files(
        fname = "{}\\{}_5x.txt".format(DATE_DIR_PATH, date),
        temp_file = 'stokes_h.txt',
        lensX = '5x'
        )
    create_files(
        fname = "{}\\{}_10x.txt".format(DATE_DIR_PATH, date),
        temp_file = 'stokes_h.txt',
        lensX = '10x'
        )
    create_files(
        fname = "{}\\{}_40x.txt".format(DATE_DIR_PATH, date),
        temp_file = 'stokes_h.txt',
        lensX = '40x'
        )
    say_is_completed()

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

def get_DATE_DIR_PATH(date):
    """Return the path of the directory 
        of data for a specific day
        
    Returns:
        str: The 'date' dir path.
    """
    DATA_DIR_PATH = _get_DATA_DIR_PATH()
    DATE_DIR_PATH = "{}\\{}".format(DATA_DIR_PATH, date)
    return DATE_DIR_PATH

def is_DATE_DIR_existed(date_dir_path):
    try:
        os.makedirs(date_dir_path)
        print("Create: '{}'".format(date_dir_path))
    except FileExistsError:
        print("Directory already exists.")

def create_files(fname, temp_file, lensX):
    try:
        with open(fname, 'x') as f:
            template = console.get_datafile_template(temp_file)
            f.write(template.format(lensX=lensX))
        print("Create: {}".format(fname))
    except FileExistsError:
        print("\"{}\" already exists.".format(fname))

def say_is_completed():
    print(
        "Creating files has been completed.\n"
        "Please input data."
        )

