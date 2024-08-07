# -*- coding: utf-8 -*-
"""Ploynomial_Linear_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18nUpi8dgT84I6UXBRe68qIXqiyZ1ussF

Polynomial Linear Regression

Import Libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

"""Importing Data and Data processing"""

df = pd.read_csv('Position_Salaries.csv')
x = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values

"""Training the Linear Regression model on the whole dataset"""

lr = LinearRegression()
lr.fit(x,y)

"""Training the Polynomial Regression model on the whole dataset"""

pr = PolynomialFeatures(degree = 4)
x_poly = pr.fit_transform(x)
lr2 = LinearRegression()
lr2.fit(x_poly, y)

"""Visualising the Linear Regression results"""

plt.scatter(x, y, color = 'green')
plt.plot(x, lr.predict(x), color = 'blue')
plt.title('True Salary or just Bluffing (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show

"""Visualising the Polynomial Regression results"""

plt.scatter(x, y, color = 'green')
plt.plot(x, lr2.predict(pr.fit_transform(x)), color = 'blue')
plt.title('True Salary or just Bluffing (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show

"""Visualising The Polynomial Regression result with smoother curve"""

x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'green')
plt.plot(x_grid, lr2.predict(pr.fit_transform(x_grid)), color = 'blue')
plt.title('True Salary or just Bluffing (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

"""Predicting a new result with Linear Regression"""

lr.predict([[6.5]])

"""Predicting a new result with Polynomial Regression"""

lr2.predict(pr.fit_transform([[6.5]]))