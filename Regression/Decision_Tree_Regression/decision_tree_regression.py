# -*- coding: utf-8 -*-
"""Decision_Tree_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ws5VE7dyY2jwlkjCcWQBAsukI9LylzFT
"""



"""Import Libraries"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

"""Importing the dataset"""

df = pd.read_csv('Position_Salaries.csv')
X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values

"""Training the Decision Tree Regression model on the whole dataset"""

dt = DecisionTreeRegressor(random_state=0)
dt.fit(X, y)

"""Predicting a new result"""

predicting_new_result = dt.predict([[6.5]])
print(predicting_new_result)

"""Visualising the Decision Tree Regression"""

x_grid = np.arange(min(X), max(X), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(x_grid, dt.predict(x_grid), color='blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()