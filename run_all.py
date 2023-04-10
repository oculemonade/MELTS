# This code runs multiple isobaric simulations using alphaMELTS
# at different pressures. alphaMELTS is prone to crashing. For this issue,
# a recursion method is implemented at the end of each pressure benchmark.
# It analyzes the bulk composition of the liquid at the point 
# of the crash and using it as input for continuing the simulation. 
# Recursion method is applied twice.
# This code is path dependent. Location of the run-alphamelts.command is
# required. A copy folder named "COPY" represents how the model will be run. 
# the .melts file for this code is called "Sudbury.melts" and is in the COPY
# folder. Editing that version will establish the bulk composition. 
# A standardized batch.txt should be in COPY as well. 
# This code is path dependent and will create folders in the location it is ran

import numpy as np
import os, re, shutil
import math as ma

# Establish which pressures the isobaric simulations should be at
pressures = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 1]
original_folder_name = 'COPY' # Every sim will be influenced by this folder
parent_folder_path = os.getcwd() # Current directory you are in

for pressure in pressures: # Looping through the established pressures
    folder_name = str(pressure) + "b_1" # Folder naming scheme
    new_folder_path = os.path.join(parent_folder_path, folder_name) # establishing path
    shutil.copytree(os.path.join(parent_folder_path, original_folder_name), new_folder_path) 
    sudbury_file_path = os.path.join(new_folder_path, "Sudbury.melts") # name of .melts file

# This will make identical folders to COPY with the updated initial pressure
    with open(sudbury_file_path, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith("Initial Pressure:"):
            lines[i] = "Initial Pressure: " + str(pressure) + "\n"
        if line.startswith("Final Pressure:"):
            lines[i] = "Final Pressure: " + str(pressure) + "\n"
    with open(sudbury_file_path, 'w') as f:
        f.writelines(lines)

    os.chdir(new_folder_path) 
    os.system('/Users/nic/Desktop/alphaMELTS2-master/bin/run-alphamelts.command < batch.txt')
    # runs alphaMELTS2, dependent on where the command file is 
    os.chdir('..')

#### Making first recursion #####
    new_folder_name = folder_name[:-1] + "2" # Makes 1000b_2, etc.
    new_folder_path = os.path.join(parent_folder_path, new_folder_name) 
    if not os.path.exists(new_folder_path):
        shutil.copytree(os.path.join(parent_folder_path, folder_name), new_folder_path)
    else:
        shutil.rmtree(new_folder_path)
        shutil.copytree(os.path.join(parent_folder_path, folder_name), new_folder_path)

    sudbury_file_path = os.path.join(new_folder_path, "Sudbury.melts")
    liquid_file_path = os.path.join(new_folder_path, "Liquid_comp_tbl.txt")
    with open(liquid_file_path, "r") as liquid:
        lines2 = liquid.read().split(' ')
    lines1 = []
    lines = []
    for sub in lines2:
        lines1.append(re.sub('\n', ' ', sub))
    for item in lines1:
        lines.extend(item.split())

    N = 16 # Number of oxides in the .melts file
    array1 = np.zeros(N)
    length = len(lines)
    percents = (lines[length - N:length + 1 ])
    words = (lines[6:6 + N])
    temp = str(ma.trunc(float(lines[ - (N + 2)]) )) # in celsius
    pres = str(lines[ - (N + 3)]) # in bars

    with open(sudbury_file_path, "w") as f:
        f.write("Title: Sudbury_Bulk_Comp_from_Original_Isobaric_Simulations\n\n")

        for i in range(N):
            array1[i] = float(percents[i])
            f.write("Initial Composition: " + words[i] + " " + percents[i] + "\n")

        f.write("\n\nInitial Temperature: " + temp + "\n")
        f.write("Final Temperature: 600\n")
        f.write("Initial Pressure: " + pres + "\n")
        f.write("Final Pressure: " + pres + "\n")
        f.write("Increment Temperature: 1.0\n")
        f.write("Increment Pressure: 0.00\n")
        f.write("dp/dt: 0\n")
        f.write("log fo2 Path: None\n")
        f.write("Mode: Fractionate Solids") # these can be edited

    os.chdir(new_folder_path)
    os.system('/Users/nic/Desktop/alphaMELTS2-master/bin/run-alphamelts.command < batch.txt')
    os.chdir('..')

#### Making second recursion #####
    third_folder_name = folder_name[:-1] + "3" #this makes 900b_3, etc
    third_folder_path = os.path.join(parent_folder_path, third_folder_name)
    if not os.path.exists(third_folder_path):
        shutil.copytree(os.path.join(parent_folder_path, folder_name), third_folder_path)
    else:
        shutil.rmtree(third_folder_path)
        shutil.copytree(os.path.join(new_folder_path, folder_name), third_folder_path)

    sudbury_file_path = os.path.join(third_folder_path, "Sudbury.melts")
    liquid_file_path = os.path.join(new_folder_path, "Liquid_comp_tbl.txt")

    with open(liquid_file_path, "r") as liquid:
        lines2 = liquid.read().split(' ')
    lines1 = []
    lines = []
    for sub in lines2:
        lines1.append(re.sub('\n', ' ', sub))
    for item in lines1:
        lines.extend(item.split())

    N = 16 # number of oxides
    array1 = np.zeros(N)
    length = len(lines)
    percents = (lines[length - N:length + 1 ])
    words = (lines[6:6 + N])
    temp = str(ma.trunc(float(lines[ - (N + 2)]) )) # in celsius
    pres = str(lines[ - (N + 3)]) # in bars

    with open(sudbury_file_path, "w") as f:
        f.write("Title: Sudbury_Bulk_Comp_from_Original_Isobaric_Simulations\n\n")

        for i in range(N):
            array1[i] = float(percents[i])
            f.write("Initial Composition: " + words[i] + " " + percents[i] + "\n")

        f.write("\n\nInitial Temperature: " + temp + "\n")
        f.write("Final Temperature: 600\n")
        f.write("Initial Pressure: " + pres + "\n")
        f.write("Final Pressure: " + pres + "\n")
        f.write("Increment Temperature: 1.0\n")
        f.write("Increment Pressure: 0.00\n")
        f.write("dp/dt: 0\n")
        f.write("log fo2 Path: None\n")
        f.write("Mode: Fractionate Solids")

    os.chdir(new_folder_path)
    os.system('/Users/nic/Desktop/alphaMELTS2-master/bin/run-alphamelts.command < batch.txt')
    os.chdir('..') #goes back a directory

## fin
