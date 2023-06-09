import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
print(os.getcwd())
import seaborn as sns
import math

#copy files from other folder to this folder
import shutil
old_path = r'/Users/haraldphilipson/PycharmProjects/RPdroplets/droplets_area.csv'
new_path = r'/Users/haraldphilipson/PycharmProjects/RPdropsDistr/droplets_area.csv'
shutil.copy(old_path, new_path)
print('Copied')

df = pd.read_csv('droplets_area.csv')

#assume 70%Si, 10%Al, 20%Ca
dSi = 2.329002
dAl = 2.7
dCa = 1.55
assigned_density = (dSi*0.7) + (dAl*0.1) + (dCa*0.2)
p = assigned_density

d1550 = df.loc[:, ['W27_M1adj', 'W28_M1adj', 'W43_M1adj']]
#stack columns of parallels to one column
part1 = d1550.iloc[:, 0]
part2 = d1550.iloc[:, 1]
part3 = d1550.iloc[:, 2]
new_column = ["stacked parallells"]
part1.columns = new_column
part2.columns = new_column
part3.columns = new_column
d1550 = pd.concat([part1, part2, part3], ignore_index=True) #stack the columns to become one column
d1550 = d1550[~np.isnan(d1550)] #removes NaNs
d1550_r = np.sqrt(d1550/math.pi) #convert the values from area to radius
d1550_m = (d1550_r**3) * (4/3)*math.pi * p #convert every particle to its mass, estimated

d1600 = df.loc[:, ['W39_M1', 'W50_M1']]
#stack columns of parallels to one column
part4 = d1600.iloc[:, 0]
part5 = d1600.iloc[:, 1]
part4.columns = new_column
part5.columns = new_column
d1600 = pd.concat([part4, part5], ignore_index=True)
d1600 = np.sqrt(d1600/math.pi) #convert area to radius
#d1600_m = (d1600**3) * (4/3)*math.pi * assigned_density #convert to mass, estimated

d1650 = df.loc[:, ['W35_M1', 'W36_M1', 'W47_M1']]
#stack columns of parallels to one column
part6 = d1650.iloc[:,0]
part7 = d1650.iloc[:,1]
part8 = d1650.iloc[:,2]
part6.columns = new_column
part7.columns = new_column
part8.columns = new_column
d1650 = pd.concat([part6, part7, part8], ignore_index=True)
d1650 = np.sqrt(d1650/math.pi) #convert area to radius
#d1650_m = (d1650**3) * (4/3)*math.pi * assigned_density #convert to mass, estimated

#colors
col1 = '#CC4F1B'
col2 = '#000080'
col3='#6B8E23'
col = ['#CC4F1B', '#000080', '#6B8E23']

#sns.set(style="darkgrid")
fig2, ax2 = plt.subplots(1, 3, figsize=(12, 5))
bins = 10000000

##### 1550 #######

#ax1 = sns.histplot(data=np.cumsum(sorted(d1550)), kde=True, alpha=0.5, color="blue", bins=100)
ax2[0].hist(d1550_r, alpha=0.5, color="blue", bins=50)
#ax1 = sns.histplot(data=np.cumsum(sorted(d1550_m)), ax=ax2[1], kde=True, alpha=0.5, color="blue", bins=50)
ax2[1].plot(np.cumsum(sorted(d1550_m)), alpha=0.5, color="blue")

# Create a new figure and axes for the separate plot

# Calculate the summed values for each bin interval
hist, edges = np.histogram(d1550_m, bins=bins)
summed_values = np.cumsum(hist) # sum
edges = ((edges*3) / (4*math.pi * p))**(1/3) # convert x-axis from mass to radius again
# Plot the summed values in a bar plot
#ax2.bar(edges[:-1], summed_values, width=np.diff(edges), align='edge', color="blue", alpha=0.5)
ax2[2].plot(edges[:-1], summed_values, color="blue", alpha=0.5)
#ax2[1].hist(sorted(np.cumsum(d1550_m)), color="blue", alpha=0.5, bins=bins)




##### 1600 #######

#sns.histplot(data=d1600, kde=True, alpha=0.3, color="olive", bins=bins)

##### 1650 #######

#sns.histplot(data=d1650, kde=True, alpha=0.2, color="red", bins=bins)




#ax1.set_xlim(0, 80)
#ax1.set_ylim(0, 350)
#ax1.set(xlabel='Radius')


# Calculate the differences between consecutive summed values
#differences = np.diff(summed_values)
# Create x-axis values
#x_values = (edges[:-1] + edges[1:]) / 2
# Plot the derivative values as a line plot
#ax11 = sns.histplot(differences, kde=True, color="blue", alpha=0.5, bins=30)

# Set the labels and title for the separate plot
#ax2.set_xlabel('Radius')
#ax2.set_ylabel('Summed Values')
#ax2.set_title('Summed Values in Each Bin Interval')

# Show the separate plot
plt.show()

#plt.legend(['1550 °C', '1600 °C', '1650 °C'])
#fig.tight_layout()
#fig.savefig('distr3min_counts_radius.svg', format='svg', dpi=1200)
