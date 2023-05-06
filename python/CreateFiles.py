import os

MAIN_DIR = os.path.dirname(__file__)
date = input("Please enter the date.\n")
DATA_DIR = "{}\\data".format(MAIN_DIR)
date_dir = "{}\\{}".format(DATA_DIR, date)

def create_files():
    # create dir
    exists_date_dir = os.path.exists(date_dir)
    if exists_date_dir == True:
        pass
    else:
        os.makedirs(date_dir)
        print("Create: '{}'".format(date_dir))

    # create files
    existsFD_DATA = os.path.exists("{}\\FiberDiameter_{}.txt".format(date_dir, date))
    if existsFD_DATA == True:
        pass
    else:
        fname = "{}\\FiberDiameter_{}.txt".format(date_dir, date)
        with open(fname, 'w') as f:
            FD_format = (
                "# Fiber Diameter\n"
                "# X: Absolute position, y1:Upper edge, y2: Lower edge\n"
                "# X, y1, y2"
                )
            f.write(FD_format)
        print("Create: {}".format(fname))
    
    
    exists_PE_5x_data = os.path.exists("{}\\{}_5x.txt".format(date_dir, date))
    if exists_PE_5x_data == True:
        pass
    else:
        fname = "{}\\{}_5x.txt".format(date_dir, date)
        with open(fname, 'w', newline='') as f:
            PE_5x_format = (
                "# Polarization Experiment\n"
                "# Step 10 -> 2, lens:5x\n"
                "# s1 s2 s3\n"
                )
            f.write(PE_5x_format)
        print("Create: {}".format(fname))
    
    
    exists_PE_10x_data = os.path.exists("{}\\{}_10x.txt".format(date_dir, date))
    if exists_PE_10x_data == True:
        pass
    else:
        fname = "{}\\{}_10x.txt".format(date_dir, date)
        with open(fname, 'w', newline='') as f:
            PE_10x_format = (
                "# Polarization Experiment\n"
                "# Step 10 -> 2, lens:10x\n"
                "# s1 s2 s3\n"
                )
            f.write(PE_10x_format)
        print("Create: {}".format(fname))
    
    
    exists_PE_40x_data = os.path.exists("{}\\{}_40x.txt".format(date_dir, date))
    if exists_PE_40x_data == True:
        pass
    else:
        fname = "{}\\{}_40x.txt".format(date_dir, date)
        with open(fname, 'w', newline='') as f:
            PE_40x_format = (
                "# Polarization Experiment\n"
                "# Step 10 -> 2, lens:40x\n"
                "# s1 s2 s3\n"
                )
            f.write(PE_40x_format)
        print("Create: {}".format(fname))
    
    print(
        "Creating files has been completed.\n"
        "Input data."
        )


create_files()