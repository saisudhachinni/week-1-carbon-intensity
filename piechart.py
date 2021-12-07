import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


dataset = pd.read_csv('https://api.carbonintensity.org.uk/regional')

dataset = ['dnogegion id', 'region', 'Forecast',
           'fuel', 'perc', 'index', 'shortname']

print(dataset)

data = [23, 17, 35, 29, 12, 41,19]



# Creating plot
explode = (0.1, 0.3, 0.2, 0.3, 0.5, 0.3,0,1)

# Creating color parameters
colors = ("orange", "cyan", "brown",
          "grey", "indigo", "beige","red")

def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)




fig = plt.figure(figsize=(17, 8))
plt.pie(data, labels=dataset)

# show plot
plt.show()
