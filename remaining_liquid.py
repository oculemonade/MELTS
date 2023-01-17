## The point of this code is to go into the liquid comp output file,
## and take the last oxide weight percents prior to crash and make a
## new .melts file with those values (temp and pressure included).
## This new .melts file is pushed back one folder
## FILE MUST BE READ IN SAME FOLDER AS OUTPUTS
## !!!! Assumes title length of 8 items !!!!

import numpy as np
import os
import re

liquid = open("Liquid_comp_tbl.txt", "r") # reads liquid file
lines2 = liquid.read().split(' ')
lines1 = []
lines = []
for sub in lines2:
    lines1.append(re.sub('\n', ' ', sub))
for item in lines1:
    lines.extend(item.split())

N = 15 # number of oxides
array1 = np.zeros(N)
length = len(lines)
percents = (lines[length - N:length + 1 ])
words = (lines[13:13 + N])
temp = str(float(lines[ - (N + 2)]) - 273.15) # in celsius
pres = str(lines[ - (N + 3)]) # in bars

f = open("NEW_Sudbury.melts","w")
f.write("Title: Sudbury Bulk Comp with Cr and traces \n \n")

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

os.system('mv NEW_Sudbury.melts ..') # pushes file back one directory