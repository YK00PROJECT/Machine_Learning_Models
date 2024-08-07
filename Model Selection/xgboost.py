# -*- coding: utf-8 -*-
"""XGBoost.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kltsxz3KankBPch19wTS-m9H1pA8hL3z

XGBoost
"""

!pip install xgboost

"""Importing Libraries"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score
from xgboost import XGBClassifier

"""Data Preprocessing"""

# Load the data and inspect the target variable
df = pd.read_csv('Data.csv')
print(df['Class'].unique())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_train = le.fit_transform(y_train)

"""Importing Dataset"""

df = pd.read_csv('Data.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

"""Splitting the dataset into the training and test set"""

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

"""Training XGBoost on the training"""

# Check the unique values in the training target variable
print(np.unique(y_train))

import numpy as np
y_train = np.where(y_train == 2, 0, 1)

classifier = XGBClassifier()
xg = classifier.fit(x_train, y_train)

"""Making cofusion matrix"""

y_pred = xg.predict(x_test)
y_pred = np.where(y_pred == 0, 2, 4)
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

"""Visualizing Confusion matrix"""

!pip install seaborn
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

"""Applying K-fold cross validation"""

accuracy_score  = cross_val_score(estimator=xg, X=x_train, y=y_train, cv=10)
print('Accuracy: {:.2f} %'.format(accuracy_score.mean()*100))
print('Standard Deviation: {:.2f} %'.format(accuracy_score.std()*100))