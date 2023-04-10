# The point of this script is to parse through the Phase mass
# text file and print out the temperatures when a phases
# shows up. A phase showing up means that its mass goes from 
# zero to nonzero. If a phase shows up twice, it will print both
# temperatures. If a phase is present during the entirety of a
# simulation, it will indicate with the initial temperature

import numpy as np

# read the file
with open('Phase_mass_tbl.txt', 'r') as file:
    lines = file.readlines()

# find the start of the phase masses section
for i, line in enumerate(lines):
    if 'Phase Masses:' in line:
        start = i

# get the phase names
header = lines[start + 1].split()
phase_names = header[4:]

# initialize a dictionary to store whether each phase has appeared yet
phase_presence = {phase: False for phase in phase_names}

# loop through the phase masses section
for line in lines[start + 2:]:
    # check if this is the end of the phase masses section
    if 'Phase' in line:
        break
    # split the line into data columns
    data = line.split()
    # get the temperature
    T = float(data[2])
    # loop through the phase masses
    for i in range(len(phase_names)):
        # check if this phase has appeared yet
        if not phase_presence[phase_names[i]]:
            # check if this phase has non-zero mass
            if float(data[i + 4]) != 0:
                print(f"{phase_names[i]} first appears at T = {T:.2f}")
                phase_presence[phase_names[i]] = True
        # else if this phase has appeared, check if it has zero mass
        elif float(data[i + 4]) == 0:
            phase_presence[phase_names[i]] = False
pressure = float(lines[start + 2].split()[1])
print(f"The pressure is {pressure:.2f}")
