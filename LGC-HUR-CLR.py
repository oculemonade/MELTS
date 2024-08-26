import matplotlib.pyplot as plt
import numpy as np

# This script creates a 4-subplot figure to show the Squared center Log Ratio
# for each major oxide of the 4 layers of the Sudbury Basin

##########################################################
###################### Input Data ########################
##########################################################

oxides = ['SiO$_2$', 'Al$_2$O$_3$', 'FeO', 'MgO', 'CaO', 'Na$_2$O']
target_MNR  = [56.20 , 10.31  , 8.36 , 13.42 , 4.43 , 1.91]
target_FNR  = [57.98 , 17.33  , 4.73 , 05.18 , 6.88 , 3.22]
target_QGAB = [55.55 , 14.60  , 7.18 , 03.56 , 6.78 , 3.90]
target_GRAN = [67.83 , 12.74  , 3.23 , 01.19 , 1.74 , 3.69]

#100% Levack Gneiss Complex
LGC100_MNR  = [55.41 , 18.24  , 5.15 , 10.29 , 6.71 , 3.61]
LGC100_FNR  = [56.18 , 21.03  , 3.90 , 06.38 , 7.27 , 4.62]
LGC100_QGAB = [56.91 , 19.65  , 5.62 , 05.18 , 6.37 , 4.93]
LGC100_GRAN = [67.92 , 11.22  , 5.84 , 01.30 , 4.41 , 3.98]

#75% Levack Gneiss Complex， 25% Huronian Supergroup
L75H25_MNR  = [55.02 , 12.14  , 9.36 , 15.88 , 4.46 , 2.42]
L75H25_FNR  = [60.61 , 19.25  , 3.92 , 4.620 , 6.35 , 4.49]
L75H25_QGAB = [68.32 , 14.48  , 4.29 , 2.380 , 4.48 , 3.64]
L75H25_GRAN = [68.95 , 12.42  , 4.76 , 0.960 , 3.70 , 3.49]

#50% Levack Gneiss Complex， 50% Huronian Supergroup
L50H50_MNR  = [64.61 , 4.000  , 11.61, 16.94 , 1.55 , 0.66]
L50H50_FNR  = [70.41 , 15.10  , 2.72 , 2.670 , 4.91 , 3.54]
L50H50_QGAB = [68.59 , 14.54  , 4.08 , 2.230 , 4.49 , 3.55]
L50H50_GRAN = [69.35 , 13.87  , 3.93 , 0.830 , 3.04 , 3.10]

#25% Levack Gneiss Complex， 75% Huronian Supergroup
L25H75_MNR  = [92.06 , 0.280  , 2.89 , 4.530 , 0.10,  0.01]
L25H75_FNR  = [74.80 , 8.940  , 5.13 , 5.390 , 2.87 , 2.04]
L25H75_QGAB = [68.76 , 14.25  , 4.38 , 1.880 , 4.29 , 3.52]
L25H75_GRAN = [69.58 , 15.25  , 3.15 , 0.590 , 2.25 , 2.69]

##########################################################

##########################################################
################ Aitchison Calculator ####################
##########################################################

def geometric_mean(data):
    return np.prod(data)**(1/len(data))

geo_means = {}
target_dict = {
    "target_MNR": target_MNR,
    "target_FNR": target_FNR,
    "target_QGAB": target_QGAB,
    "target_GRAN": target_GRAN,
    "LGC100_MNR": LGC100_MNR,
    "LGC100_FNR": LGC100_FNR,
    "LGC100_QGAB": LGC100_QGAB,
    "LGC100_GRAN": LGC100_GRAN,
    "L75H25_MNR": L75H25_MNR,
    "L75H25_FNR": L75H25_FNR,
    "L75H25_QGAB": L75H25_QGAB,
    "L75H25_GRAN": L75H25_GRAN,
    "L50H50_MNR": L50H50_MNR,
    "L50H50_FNR": L50H50_FNR,
    "L50H50_QGAB": L50H50_QGAB,
    "L50H50_GRAN": L50H50_GRAN,
    "L25H75_MNR": L25H75_MNR,
    "L25H75_FNR": L25H75_FNR,
    "L25H75_QGAB": L25H75_QGAB,
    "L25H75_GRAN": L25H75_GRAN,
}

for key in target_dict:
    geo_means[key] = geometric_mean(target_dict[key])

def clr(data, target, geo_means):
    return [
        (np.log(data[i] / geo_means[data_name]) - np.log(target[i] / geo_means[target_name]))**2
        for i in range(len(data)) ]

##########################################################

# Dictionary for each of the layers of each simulation
clr_dict = {}
for prefix in ["LGC100", "L75H25", "L50H50", "L25H75"]:
    for rock_type in ["MNR", "FNR", "QGAB", "GRAN"]:
        data_name = f"{prefix}_{rock_type}"
        target_name = f"target_{rock_type}"
        clr_dict[data_name] = clr(target_dict[data_name], target_dict[target_name], geo_means)

##########################################################
####################### Plotting #########################
##########################################################
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
titles = ['Mafic Norite', 'Felsic Norite', 'Quartz Gabbro', 'Granophyre']
clr_keys = ["MNR", "FNR", "QGAB", "GRAN"]

# Add or remove simulations here
legend_labels = {
    "LGC100": "100% LGC",
    "L50H50": "LGC-Huronian 50-50%",
    "L25H75": "LGC-Huronian 25-75%",
    "L75H25": "LGC-Huronian 75-25%",
}

for idx, rock_type in enumerate(clr_keys):
    row, col = divmod(idx, 2)
    ax = axs[row, col]
#   Establish the colors for each simulation here
    for prefix, color in zip(["LGC100", "L50H50", "L25H75", "L75H25"], ['r', 'g', 'y', 'm', 'c']):
        data_name = f"{prefix}_{rock_type}"
        ax.plot(oxides, clr_dict[data_name], marker='o', linestyle='-', color=color, label=legend_labels[prefix])
    ax.set_yscale('log')
    ax.set_ylim(1e-7, 1e2)
    ax.set_title(titles[idx], fontweight='bold')
    
    # Only add y-axis label and legend to the first column
    if col == 0:
        ax.set_ylabel('Squared Center Log Ratio', fontsize=12, fontweight='bold')
        if idx == 0:
            ax.legend(prop={'weight': 'bold'})
    else:
        # Remove y-axis tick labels on the right plots
        ax.set_yticklabels([])
    
    # Add grid and format ticks
    ax.grid(True)
    ax.tick_params(axis='y', which='major', labelsize=14)
    ax.set_xticklabels(oxides, fontsize=12, fontweight='bold')
    for label in ax.get_yticklabels():
        label.set_fontsize(13)
        label.set_fontweight('bold')

fig.suptitle('Levack Gneiss Complex and Huronian Supergroup Input', fontsize=16, fontweight='bold')
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.tight_layout()
plt.show()
##########################################################
