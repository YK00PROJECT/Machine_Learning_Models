# -*- coding: utf-8 -*-
"""Natural_Language_Processing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lQJhBIN5kqSESFHvX92OYs68uG7yOF_7

Natural Language Processing(NLP)

Importing Libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

"""Importing Dataset

"""

df = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

"""Cleaning the texts"""

corpus = []
for i in range(0,1000):
  review = re.sub('[^a-zA-Z]', ' ', df['Review'][i])
  review = review.lower().split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)
  corpus.append(review)

"""To find out the max_features for CountVectorization"""

cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()
y = df.iloc[:, -1].values

display(corpus)

len(x[0])

"""Creating the Bag of Words model"""

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = df.iloc[:, -1].values

"""Splitting the dataset into training and test set"""

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""Training the Naive Bayes model on training set"""

classifier = GaussianNB()
classifier.fit(x_train, y_train)

"""Predicting the test set results"""

y_pred = classifier.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""Making the Confusion Matrix"""

cf = confusion_matrix(y_test, y_pred)
print(cf)
accuracy_score(y_test, y_pred)

"""Visualization of the result"""

# Creating the confusion matrix visualization
cm = confusion_matrix(y_test, y_pred, labels=classifier.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classifier.classes_)

# Plot the confusion matrix
disp.plot()
plt.show()