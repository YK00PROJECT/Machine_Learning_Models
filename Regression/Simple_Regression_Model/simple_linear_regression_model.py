# -*- coding: utf-8 -*-
"""Simple_Linear_regression_Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19AspwF4CnF08mGly4AYcjMrGsgbPj5yK

Simple_Linear_regression_Model

Importing Library
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

"""Importing the data and Splitting the dataset into the Training set and Test set"""

df = pd.read_csv("Salary_Data.csv")
df.head()
x = df.drop('Salary',axis =1)
y = df['Salary']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 1)
display(x_train,y_train)

"""Training the Simple Linear Regression model on the Training set"""

lr =LinearRegression()
lr.fit(x_train,y_train)

"""Predictive the Test set results"""

y_pred = lr.predict(x_test)
display(y_pred)

"""Visualising the Training set results"""

plt.scatter(x_train,y_train,color = 'green')
plt.plot(x_train,lr.predict(x_train),color = 'red')
plt.title('Salary vs Experience(Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary)')
plt.show()

"""Visualising the Test set results"""

plt.scatter(x_test,y_test,color = 'black')
plt.plot(x_train,lr.predict(x_train),color = 'blue')
plt.title('Salary vs Experience(Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary)')
plt.show()

"""Making a single prediction the salary of an employee with 20 years of experience?"""

print(lr.predict([[20]]))

"""Obtaining the final linear regression equation with the values of the coefficients?"""

print(lr.coef_)
print(lr.intercept_)