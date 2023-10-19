# Diabetes Predictor using Random Forest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from warnings import simplefilter

simplefilter(action='ignore',category = FutureWarning)

df = pd.read_csv('diabetes.csv')
sep = '-'*80

print("Columns of dataset :", df.columns)
print(sep)

print("Shape of dataset :", df.shape)
print(sep)

print("First 5 records of dataset :", df.head())
print(sep)

X_train, X_test, y_train, y_test = train_test_split(df.loc[:,df.columns != 'Outcome'],df['Outcome'], stratify=df['Outcome'], random_state = 34)

rf = RandomForestClassifier(n_estimators = 100, random_state = 0)
rf.fit(X_train,y_train)

print(sep)

print("Accuracy on training set : {:.3f}".format(rf.score(X_train,y_train)))
print("Accuracy on test set : {:.3f}".format(rf.score(X_test,y_test)))

print(sep)

rf1 = RandomForestClassifier(max_depth =3, n_estimators = 100, random_state = 0)
rf.fit(X_train, y_train)

print("Accuracy on training set : {:.3f}".format(rf1.score(X_train,y_train)))
print("Accuracy on test set : {:.3f}".format(rf1.score(X_test,y_test)))
print(sep)

def plot_feature_importance(model):
    plt.figure(figsize =(8,6))
    n_features = 8

    plt.barh(range(n_features),model.feature_importance_,align='center')
    df_features = [x for i, x in enumerate(df.columns) if i!=8]
    plt.yticks(np.arange(n_features),df_features)
    plt.xlabel('Feature importance')
    plt.ylabel('Feature')
    plt.ylim(-1,n_features)
    plt.show()

plot_feature_importance(rf)
