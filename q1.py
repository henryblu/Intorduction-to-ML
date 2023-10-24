import pandas as pd
import matplotlib.pyplot as plt

# Problem 1.
## 1. loads the data set in x.csv, into a pandas dataframe.
data = pd.read_csv('x.csv', header=None)
data.columns = data.iloc[0]
data = data.drop(0, axis=0)
data = data.astype(float)
print(data)

## 2. finds the two variables having the largest variances
varience = data.var().sort_values(ascending=False)
sorted_data = data[varience.index]
highest_variences = sorted_data.iloc[:, 0:2]
print(f"largest var: {highest_variences.columns[0]}")
print(f"Second largest var: {highest_variences.columns[1]}")

## 3. makes a scatterplot of the data items using these two variables
plt.scatter(highest_variences.iloc[:, 0], highest_variences.iloc[:, 1])
plt.xlabel(highest_variences.columns[0])
plt.ylabel(highest_variences.columns[1])
plt.show()