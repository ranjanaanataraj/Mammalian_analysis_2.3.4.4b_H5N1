import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define the sets A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7,8}

# Create a Venn diagram
plt.figure(figsize=(8, 8))
venn = venn2([A, B], ('A', 'B'))

# Set custom colors
venn.get_patch_by_id('10').set_color('lightblue')  # A - B region
venn.get_patch_by_id('01').set_color('lightcoral')  # B - A region
venn.get_patch_by_id('11').set_color('lavender')  # A ∩ B region

# Highlight the area corresponding to A - B  and B-A with dashed lines
venn.get_patch_by_id('10').set_edgecolor('white')
venn.get_patch_by_id('10').set_alpha(0.9)
venn.get_patch_by_id('10').set_hatch('//')  # Use // for dashed lines at 45 degrees
venn.get_patch_by_id('10').set_linewidth(2.5)


venn.get_patch_by_id('01').set_edgecolor('white')
venn.get_patch_by_id('01').set_alpha(0.9)
venn.get_patch_by_id('01').set_hatch('//')   # Set the part of B not in A to be very light
venn.get_patch_by_id('10').set_linewidth(2.5)

venn.get_patch_by_id('11').set_alpha(0.7)   # Set the intersection part to be very light

for label in venn.set_labels:
    label.set_text('')  # Clear set labels (A, B)
for subset in venn.subset_labels:
    if subset:
        subset.set_text('')  # Clear subset labels (10, 01, 11)

# Display the diagram
#plt.title('Venn Diagram of A - B with Dashed Lines')
plt.savefig("/Users/ranjananataraj/Desktop/venn_1.tiff",dpi = 600)
plt.show()
