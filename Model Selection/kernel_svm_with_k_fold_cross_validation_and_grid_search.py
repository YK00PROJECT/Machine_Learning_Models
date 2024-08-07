# -*- coding: utf-8 -*-
"""Kernel_SVM_With_K_Fold_Cross_Validation_And_Grid_Search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cv4DNTLCl3L98qc5ws9Z4XJz8cfH5XY9

Kernel_SVM

Import Libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

"""Importing dataset and splitting dataset into training and test sets"""

pd = pd.read_csv('Social_Network_Ads.csv')
X = pd.iloc[:, :-1].values
y = pd.iloc[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

"""Feature Scaling"""

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

"""Training the Logistic Regression model on the training set"""

classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(x_train, y_train)

"""Predicting a new result"""

print(classifier.predict(sc.transform([[30,87000]])))

"""Predicting the test set result"""

y_predict = classifier.predict(x_test)
display(y_predict)

print(np.concatenate((y_predict.reshape(len(y_predict),1), y_test.reshape(len(y_test),1)),1))

"""Making the confusion matrix"""

confusion_matrix(y_test, y_predict)

accuracy_score(y_test, y_predict)

cm = confusion_matrix(y_test, y_predict, labels=classifier.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=classifier.classes_)
disp.plot()
plt.show()

"""Applying K-fold cross validation"""

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = x_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))

"""Applying Grid Search"""

parameters = [{'C':[0.25,0.5,0.75,1],'kernel':['linear']},
              {'C':[0.25,0.5,0.75,1],'kernel':['rbf'],'gamma':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]}]
grid_search = GridSearchCV(estimator = classifier,
                           param_grid = parameters,
                           scoring = 'accuracy',
                           cv = 10,
                           n_jobs = -1)
grid_search.fit(x_train, y_train)
best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_
print("Best Accuracy: {:.2f} %".format(best_accuracy*100))
print("Best Parameters:", best_parameters)

"""Visualising the Training set results"""

plt.scatter(x_train[:, 0], x_train[:, 1], c = y_train, cmap = 'rainbow')

from matplotlib.colors import ListedColormap
x_set, y_set =  sc.inverse_transform(x_train), y_train
X1, X2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 10, stop = x_set[:, 0].max() + 10, step = 1),
                     np.arange(start = x_set[:, 1].min() - 1000, stop = x_set[:, 1].max() + 1000, step = 1))
plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('white', 'yellow')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

"""Visualising the Test set results"""

plt.scatter(x_test[:, 0], x_test[:, 1], c = y_test, cmap = 'rainbow')

from matplotlib.colors import ListedColormap
x_set, y_set =  sc.inverse_transform(x_test), y_test
X1, X2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 10, stop = x_set[:, 0].max() + 10, step = 1),
                     np.arange(start = x_set[:, 1].min() - 1000, stop = x_set[:, 1].max() + 1000, step = 1))
plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('white', 'yellow')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()