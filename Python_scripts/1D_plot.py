import matplotlib.pyplot as plt
import numpy as np

# Your data points
positions = [0.02,0.04,-0.06,0.18,-0.04]
colors = ['red', 'blue', 'green', 'orange', 'magenta']  # Different colors for each point

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot a horizontal line at y=0
ax.axhline(0, color='grey')

dot_size = 10
border_width = 1
border_color = "black"
# Plot the points on the line with different colors
for pos, color in zip(positions, colors):
    ax.plot(pos, 0, 'o', color=color,markersize=dot_size, markeredgewidth=border_width, markeredgecolor=border_color)

# Annotate the points with their values
for pos in positions:
    ax.text(pos, 0.1, f'{pos}', ha='center')


ax.set_xlim(-0.1, 0.4)
ax.set_xticks(np.arange(-0.1, 0.5,0.1))

# Remove y-axis as it's not needed
ax.get_yaxis().set_visible(False)

plt.savefig("/Users/ranjananataraj/Desktop/raccoon_1D.pdf")
# Show the plot
plt.show()
