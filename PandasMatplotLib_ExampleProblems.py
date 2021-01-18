# Real World Examples

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# LINE GRAPH
gas = pd.read_csv('gas_prices.csv')
# Make a line plot for the gas prices for each country over the year
plt.title('Gas Prices Over Time (in USD)', fontdict={'fontweight': 'bold', 'fontsize':22})
# plt.plot(gas['Year'], gas['USA'], 'b.-', label='USA')
# plt.plot(gas['Year'], gas['Canada'], 'r.-', label='Canada')
# plt.plot(gas['Year'], gas['South Korea'], 'g.-', label='South Korea')
# plt.plot(gas['Year'], gas['Australia'], 'y.-', label='Australia')
for country in gas[1:]:
    if country != 'Year':
        plt.plot(gas.Year, gas[country], marker='.', label=country)
plt.legend()
plt.xlabel('Year')
plt.ylabel('US Dollars')
# This makes the x ticks every three years. Add an extra year of 2011
plt.xticks(gas.Year[::3].tolist()+[2011])
# Save the figure
plt.savefig('Gas_Price_Figure.png', dpi=300)
plt.show()

# MOVING ON TO FIFA DATA
fifa = pd.read_csv('fifa_data.csv')
print(fifa)

# FIFA HISTOGRAM EXAMPLE
# Plot how many people at each skill level region
# Create the plot
# Create the bins at intervals of 10
bins = [40,50,60,70,80,90,100]
plt.hist(fifa['Overall'], bins=bins, color='r')
# Make the x ticks the bins
plt.xticks(bins)
plt.ylabel('Number of Players')
plt.xlabel('Skill Level')
plt.title('Distribution of Players skills in Fifa 2018')
plt.show()

# FIFA PIE CHARTS EXAMPLE
# Do a pie chart on percentage of people who play with their left foot versus their right foot.
# First calculate the number of players that prefer their left or right feet
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
labels = ['Left Preferred', 'Right Preferred']
colors = ['r','b']
# Add in the parameters. use '% .2f %%' to show the percents to 0.2 accuracy. The second % ensures that the symbol will
# show up on the graph.
plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')
plt.title('Foot Preference of Fifa Players')
plt.show()

# MORE COMPLICATED FIFA PIE CHART EXAMPLE
# Plot the breakdown of the weights of the fifa players.
# Must first reset the weight values from a string to an integer
fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
# Now create the different weight classes
light = fifa.loc[fifa['Weight'] < 125].count()[0]
light_medium = fifa.loc[(fifa['Weight'] >= 125) & (fifa['Weight'] < 150)].count()[0]
medium = fifa.loc[(fifa['Weight'] >= 150) & (fifa['Weight'] < 175)].count()[0]
medium_heavy = fifa.loc[(fifa['Weight'] >= 175) & (fifa['Weight'] < 200)].count()[0]
heavy = fifa.loc[fifa['Weight'] >= 200].count()[0]
# Classify the different weight classes
weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['Light (< 125lbs)', 'Light-Medium (125 lbs - 150 lbs)', 'Medium (150 lbs - 175 lbs)', 'Medium-Heavy (175 lbs - 200 lbs)', 'Heavy ( >200 lbs)']
explode = (0.5, 0.1, 0, 0, 0.5)
# Changes the color scheme
plt.style.use('ggplot')
# Create the plot
plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode)
plt.title('Distribution of Weight of all FIFA Players (in lbs)')
plt.show()

# BOX AND WHISKER PLOT
# Comparing relative strength of different teams by stats
# Extract the overall ratings of each player for several teams
barcelona = fifa.loc[fifa['Club'] == 'FC Barcelona']['Overall']
real_madrid = fifa.loc[fifa['Club'] == 'Real Madrid']['Overall']
juventus = fifa.loc[fifa['Club'] == 'Juventus']['Overall']
new_england_revs = fifa.loc[fifa['Club'] == 'New England Revolution']['Overall']
labels=['FC Barcelona', 'Real Madrid', 'Juventus', 'New England Revolution']
# Plot a box and whiskers plot for these.
plt.figure(figsize=(5, 8))
# The patch artist = true property allows you to change the face color
boxes = plt.boxplot([barcelona, real_madrid, juventus, new_england_revs], labels=labels, patch_artist=True, medianprops={'linewidth': 2})
plt.style.use('default')
plt.ylabel('Overall Player Rating')
plt.xlabel('Team')
plt.title('Box and Whisker Plot Distribution of Overall Rating of all Players for Teams')
for box in boxes['boxes']:
    # Set edge color
    box.set(color='#4286f4', linewidth=2)
    # Change Fill Color
    box.set(facecolor='#e0e0e0')
plt.show()
