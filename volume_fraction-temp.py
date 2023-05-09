### To be read inside simulation folder. This code will plot the phase
### fractions as a function of temperature. If there are multiple phases
### with the same name, they will be summed and combined (i.e., if there
### exists orthopyroxene1 and orthopyroxene2, they will be summed together
### You can see the values plotted in the output file that is titled
### "Phase_vol_tbl_edited.txt" 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# determine the pressure of the simulation
with open('Phase_vol_tbl.txt') as f:
    pressure = f.readlines()[2].split()[1]

# read the data into a pandas dataframe, skip the first row
df = pd.read_csv('Phase_vol_tbl.txt', delim_whitespace=True, skiprows=1)

# drop the first, second, and fourth columns (irrelevant info)
df = df.drop(columns=[df.columns[0], df.columns[1], df.columns[3]])

# drop the "fluid1" and "fluid2" column if it exists
if "fluid1" in df.columns:
    df = df.drop(columns="fluid1")
if "fluid2" in df.columns:
    df = df.drop(columns="fluid2")

# remove the number from the end of the phase names
df.columns = [re.sub(r'\d+$', '', col) for col in df.columns]

# combine duplicate columns for the same phase
df = df.groupby(df.columns, axis=1).sum()

# drop rows where the sum of the volumes is 0
df = df[df.iloc[:, 2:].sum(axis=1) != 0]

# add a column that sums the values in each row except the first two columns
df['row_sum'] = df.iloc[:, 1:].sum(axis=1)

# add a new column for each mineral that is their initial value divided by the row's total
for col in df.columns[1:-1]:
    df[col + '_frac'] = df[col] / df['row_sum']

# save the edited dataframe to a new file
df.to_csv('Phase_vol_tbl_edited.txt', sep='\t', index=False)

# define a dictionary of mineral names and their corresponding colors
mineral_colors = {
    'alkali-feldspar': 'blue',
    'orthopyroxene': 'purple',
    'olivine': 'olive',
    'rutile' : 'pink',
    'apatite' : 'orange', 
    'clinopyroxene' : 'red',
    'spinel' : 'gray', 
    'tridymite' : 'gold',
    'plagioclase' : 'black',
    'sphene' : 'turquoise',
    'quartz' : 'steelblue',
    'perovskite' : 'yellow',
    'ortho-oxide' : 'hotpink',
    'rhm-oxide' : 'brown',
    'aenigmatite' : 'turquoise',
    'garnet' : 'rosybrown',
    'alloy-liquid' : 'maroon',
    'alloy-solid' : 'midnightblue',
}


fig, ax = plt.subplots(figsize=(12, 7))
fig.subplots_adjust(right=0.8)
for col in df.columns:
    if col.endswith('_frac'):
        mineral_name = col[:-5]
        color = mineral_colors.get(mineral_name, 'black')  # use black if mineral name not in dictionary
        ax.plot(df[col], df['Temperature'], label=mineral_name, linewidth=3, color=color)
ax.set_ylabel('Temperature (C)')
ax.set_xlabel('Mineral Fraction')
ax.set_title('Temperature vs. Mineral Volume Fractions at ' + pressure + ' bars')
ax.xaxis.set_ticks(np.arange(0, 1.1, 0.1))
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
ax.grid()
plt.show()
