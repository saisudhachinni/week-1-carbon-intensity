import pandas as pd
from matplotlib import pyplot as plt

dataset = pd.read_csv('https://api.carbonintensity.org.uk/regional')

dataset = ['dnogegion id', 'region', 'Forecast',
           'fuel', 'perc', 'index', 'shortname']

print(dataset)

left = [1, 2, 3, 4, 5, 6, 8]

# heights of bars
height = [10, 24, 36, 40, 5, 20, 25]

# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('carbon intensity bar graph')

# function to show the plot
plt.show()
