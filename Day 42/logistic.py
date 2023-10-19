#Diabetes predictor using logistic regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from warnings import simplefilter

print("Diabetes Predictor using Logistic Regression")
sep = '-'*80
print(sep)

df = pd.read_csv('diabetes.csv')

print("Columns of dataset :", df.columns)
print(sep)

print("5 records of dataset")
print(df.head())
print(sep)

print("Dimension of dataset :", df.shape)
print(sep)

X_train, X_test, y_train, y_test = train_test_split(df.loc[:,df.columns != 'Outcome'], df['Outcome'], stratify = df['Outcome'], random_state = 56)

logreg = LogisticRegression().fit(X_train,y_train)

print("Training set accuracy : {:.3f}".format(logreg.score(X_train,y_train)))
print("Testing set accuracy : {:.3f}".format(logreg.score(X_test,y_test)))
print(sep)

logreg1 = LogisticRegression(C=0.01).fit(X_train,y_train)

print("Training set accuracy : {:.3f}".format(logreg1.score(X_train,y_train)))
print("Testing set accuracy : {:.3f}".format(logreg1.score(X_test,y_test)))
print(sep)




