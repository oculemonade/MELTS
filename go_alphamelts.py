##  This program does all the dirty work and starts melts
##  and loads in the environment and .melts file, which 
##  be easily changed with proper naming schemes/paths!

import os

os.system('/Users/nic/Desktop/alphaMELTS2-master/bin/run-alphamelts.command < batch.txt')
os.system('python3 next_sim2.py')
