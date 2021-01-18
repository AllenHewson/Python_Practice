# https://www.youtube.com/watch?v=DAQNHzOcO5A & https://www.youtube.com/watch?v=0P7QnIQDBJY
# Data visualization

# INSTALL LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# MATPLOTLIB DOCUMENTATION: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html

# BASIC GRAPH STUFF


# Plotting basic line graph of x and y (1D Arrays): plt.plot(x,y)
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]
# Resizing the graph (Play around with the size)
# plt.figure(figsize=(2, 1.5), dpi=300)
# Creating the line Graph
graph = plt.plot(x, y, label='2x')
# Adding Line Number Two (x2 squared)
x2 = np.arange(0,4.5,0.5)
plt.plot(x2, x2**2, 'r', label='x^2')
# Add a title
plt.title('Our First Graph')
# Add axis labels
plt.xlabel('X axis')
plt.ylabel('Y axis')
# Adding a legend to the graph. The legend will be the label specified in the graph definition above
plt.legend()

# EDITING AESTHETICS OF GRAPH
# Editing the text of titles and labels
plt.title('Our First Graph!', fontdict = {'fontname': 'Comic Sans MS', 'fontsize': 20, 'color': 'Blue'})
# Changing graph tick size
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4, 6, 8, 8.5, 10])
# Change color of the line, line width, marker shape, marker size, etc. is done in the definition of the plot. Can be
# hexidecimal color
graph = plt.plot(x, y, label='2x', color='red', linewidth=2, marker='.', markersize=10, markeredgecolor='blue', linestyle='--')
# Shorthand notation for this is '[color][marker][linestyle]'
plt.plot(x,y, 'r.-', label ='2x')
plt.show()
# SAVING THE GRAPH
plt.savefig('mygraph.png')

# Creating a bar chart
labels = ['A', 'B', 'C']
values = [1, 4, 2]
bars = plt.bar(labels, values)
# Can resize and add titles, labels, etc.
# Set the hatch pattern on the bar graph
bars[0].set_hatch('/')
bars[1].set_hatch('o')
bars[2].set_hatch('*')
# DISPLAY THE GRAPH
plt.show()

