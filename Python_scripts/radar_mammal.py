import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.font_manager import FontProperties

# Load the data
df = pd.read_csv("/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/radar_plot/data/radar_plot_4b_analysis.csv")

# Replace some values with "NA" as in your original code
df["Protein"].loc[3:5] = "NA"

# Print the dataframe to check
print(df)

# Get unique protein names and map them to angles
unique_proteins = df["Protein"].unique()
num_proteins = len(unique_proteins)
angles = np.linspace(0, 2 * np.pi, num_proteins, endpoint=False)

# Create a dictionary to map protein names to angles
protein_to_angle = {protein: angle for protein, angle in zip(unique_proteins, angles)}

# Map the protein column to angles
theta = df["Protein"].map(protein_to_angle)

r = (df["dist"])

# Create a polar scatter plot
plt.figure(figsize=(13, 10))
ax = plt.subplot(111, projection='polar')
scatter = ax.scatter(theta, r, c=df["Host type"].astype('category').cat.codes, s=df["Count_same"]*20, cmap='viridis', alpha=1 , edgecolor='black',linewidth = 1)


# Annotate HA points


# Set radial axis ticks at specific theta value (position the radial labels at HA angle)
if 'HA' in protein_to_angle:
    ha_theta = protein_to_angle['HA']
    ax.set_rlabel_position(np.degrees(ha_theta))

ax.yaxis.grid(True, alpha = 0.3)
ax.set_ylim(-2,12.5)
ax.set_yticks(np.arange(1,11,1))

# Add a color bar for the host type as a categorical variable
host_types = df["Host type"].astype('category').cat.categories
cmap = plt.get_cmap('viridis', len(host_types))
norm = mcolors.BoundaryNorm(np.arange(-0.5, len(host_types)), cmap.N)

#cbar = plt.colorbar(scatter, ax=ax, ticks=np.arange(len(host_types)), #boundaries=np.arange(len(host_types) + 1) - 0.5, norm=norm)
#cbar.set_label('Host type')
#cbar.set_ticklabels(host_types)

# Set the xticks to be the protein names
ax.set_xticks(angles)
ax.set_xticklabels(unique_proteins)
ax.tick_params(axis='x', labelsize=30, pad=20)
ax.tick_params(axis='y', labelsize=8, pad=10)

font_properties_x = FontProperties(weight='bold', size=20)  # Adjust size as needed
for label in ax.get_xticklabels():
    label.set_fontproperties(font_properties_x)

font_properties_y = FontProperties(weight='bold', size=10)
for label in ax.get_yticklabels():
    label.set_fontproperties(font_properties_y)

#handles = [plt.scatter([], [], s=size*50, color='gray', edgecolor='black') for size in [1, 2, 3]]
#labels = ['5', '10', '15']
#legend = plt.legend(handles, labels, title="Number of sequences", scatterpoints=1, loc='upper #right', bbox_to_anchor=(1.1, 1.1), prop={'size': 12})
#plt.gca().add_artist(legend)

# Display the plot
plt.savefig("/Users/ranjananataraj/Desktop/radar_mammalian_proteins.tiff",dpi = 600)

plt.show()
