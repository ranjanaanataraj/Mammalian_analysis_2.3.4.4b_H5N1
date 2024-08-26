import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV data into a DataFrame
df_HA = pd.read_csv("/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/A_C_SL_M/data/heatmap_data/A_C_SL_M_HA_data.csv")

# Set the index to "Position"
df_HA.set_index("Position", inplace=True)

# Round the values in the DataFrame to two decimal points
df_HA = df_HA.round(2)

# Create a mask for values greater than 0.01
mask = df_HA <= 0.01

# Load the CSV data into an annotations DataFrame
annot_df_HA = pd.read_csv("/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/A_C_SL_M/data/heatmap_data/A_C_SL_M_HA_annot.csv")

# Set the index to "Position"
annot_df_HA.set_index("Position", inplace=True)

# Create a custom annotations DataFrame based on the condition (not equal to '-')
custom_annotations = annot_df_HA.applymap(lambda x: x if x != '-' else '')

# Create the heatmap with custom annotations
sns.set(font_scale=2)
plt.figure(figsize=(6, len(df_HA)))  # Adjust the figure size as needed

heatmap = sns.heatmap(df_HA, annot=custom_annotations, fmt="",
                      cmap=sns.cubehelix_palette(dark=0.25, light=.99, as_cmap=True),
		       #cmap=sns.cubehelix_palette(start = 2 ,dark=0.2, light=1, as_cmap=True),
                      linewidths=0.75, cbar=False, vmin=50, vmax=100, square=True, xticklabels = True,linecolor="black", mask=mask)

# Customize the x-tick labels to include the two-line label
xtick_labels = list(annot_df_HA.columns)
xtick_labels[0] = 'Residues tolerated \nin avian H5N1'  # Assuming the third column is the one to modify
xtick_labels[1] = 'Avian' 
xtick_labels[2] = 'Mammal' 
xtick_labels[3] = 'Sea lion' 
xtick_labels[4] = 'Cattle' 
xtick_labels[5] = 'Fox' 
xtick_labels[6] = 'Hu H1N1' 
xtick_labels[7] = 'Hu H3N2' 
heatmap.set_xticklabels(xtick_labels, rotation=90, ha='center')

#heatmap.set_xticklabels(xtick_labels, rotation=90, ha='center')
# Make the spines visible and adjust their properties
for _, spine in heatmap.spines.items():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(0.5)

# Add x and y axis titles
heatmap.xaxis.tick_top()
plt.ylabel("HA", rotation=90, labelpad=10, fontweight="bold", fontsize=24)
plt.yticks(rotation=0)

# Add a vertical line to separate y-axis label and y-axis tick labels
plt.gca().add_line(plt.Line2D([0, 0], [0, 1], color='black', linewidth=1.5, transform=plt.gca().transAxes))

# Save the heatmap to a file
plt.savefig('/Users/ranjananataraj/Desktop/HA.tiff', dpi=600, bbox_inches='tight')

plt.show()
