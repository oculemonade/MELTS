import matplotlib.pyplot as plt
import numpy as np

# This code plots the Aitchison Distance vs. increasing amounts 
# of LGC%s for each of the layers of the SIC 
# The y-axis is log scale 
x_values = np.arange(0, 101, 5)  # From 0% to 100% LGC

# Data for each percentage of LGC
#         0%.      5%      10%     15%.   20%    25%    30%    35%    40%    45%    50%    55%    60%    65%    70%    75%    80%    85%    90%    95%    100%
Total = [np.nan, np.nan, np.nan, np.nan, 4.199, 3.593, 3.3  , 3.11 , 2.989, 2.882, 1.609, 1.118, 1.042, 1.002, 0.936, 0.905, 0.905, 0.907, 0.874, 1.109, 1.273]
MNR   = [np.nan, np.nan, np.nan, np.nan, 2.928, 2.483, 2.324, 2.223, 2.143, 2.027, 0.669, 0.179, 0.122, 0.119, 0.103, 0.098, 0.093, 0.115, 0.095, 0.324, 0.453]
FNR   = [np.nan, np.nan, np.nan, np.nan, 0.592, 0.444, 0.329, 0.267, 0.241, 0.25 , 0.336, 0.333, 0.309, 0.256, 0.203, 0.182, 0.17 , 0.176, 0.177, 0.182, 0.191]
QGAB  = [np.nan, np.nan, np.nan, np.nan, 0.326, 0.32 , 0.312, 0.304, 0.304, 0.302, 0.297, 0.286, 0.288, 0.3  , 0.29 , 0.276, 0.287, 0.267, 0.237, 0.223, 0.231]
GRAN  = [np.nan, np.nan, np.nan, np.nan, 0.353, 0.346, 0.335, 0.316, 0.301, 0.303, 0.307, 0.32 , 0.323, 0.327, 0.34 , 0.349, 0.355, 0.349, 0.365, 0.38 , 0.398]

plt.figure(figsize=(10, 6))

plt.plot(x_values, Total, label='Aitch', linewidth=2)
plt.plot(x_values, MNR  , label='MNR'  , linewidth=2)
plt.plot(x_values, FNR  , label='FNR'  , linewidth=2)
plt.plot(x_values, QGAB , label='QGAB' , linewidth=2)
plt.plot(x_values, GRAN , label='GRAN' , linewidth=2)

plt.ylim((10**(-1.2),10))
plt.xlabel('Percentage of LGC', fontweight='bold')
plt.ylabel('Aitchison Distance', fontweight='bold')
plt.title('Aitchison Distance vs Huronian Supergroup with Increasing LGC Content for Different Layers', fontweight='bold')

plt.yscale('log')

plt.legend(fontsize='medium', loc='best', prop={'weight':'bold'})

plt.xticks(np.arange(0, 101, 10), fontweight='bold')  # Major ticks every 10 with bold numbers
plt.yticks(fontweight='bold')  # Make y-axis numbers bold
plt.minorticks_on()  # Turn on minor ticks

plt.grid(True, which='major', linestyle='-', linewidth=0.5)  # Major grid lines
plt.grid(True, which='minor', linestyle=':', linewidth=0.5, axis='y')  # Minor grid lines on the y-axis

plt.show()