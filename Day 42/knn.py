# Daibetes predictor using KNN algorithm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('diabetes.csv')
sep = '-'*80

print("Diabetes predictor using KNN algorithm")
print("Columns of dataset :", df.columns)
print(sep)

print("First 5 rows of dataset :", df.head())
print(sep)

print("Dimension of dataset :", df.shape)
print(sep)

X_train, X_test, y_train, y_test = train_test_split(df.loc[:,df.columns !='Outcome'],df['Outcome'],random_state = 56, stratify = df['Outcome'])

training_accuracy = []
test_accuracy = []

#try n neighbors form 1 to 10

neighbors_settings = range(1,11)

for n in neighbors_settings:
    knn = KNeighborsClassifier(n_neighbors = n)
    knn.fit(X_train, y_train)

    training_accuracy.append(knn.score(X_train, y_train))
    test_accuracy.append(knn.score(X_test,y_test))

plt.plot(neighbors_settings, training_accuracy, label = 'Training accuracy')
plt.plot(neighbors_settings, test_accuracy, label = 'Test accuracy')

plt.ylabel('Accuracy')
plt.xlabel('Neighbors')
plt.legend()
plt.savefig('knn_compare_model')
plt.show()

knn = KNeighborsClassifier(n_neighbors = 9)
knn.fit(X_train,y_train)

print("Accuracy of KNN algorithm on test set :", knn.score(X_test, y_test))