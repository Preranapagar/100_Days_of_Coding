#Diabetes predictor using Decision tree

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("Diabetes Predictor using Decision Tree")

df = pd.read_csv("diabetes.csv")

print("Columns of Dataset")
print(df.columns)

print("First 5 records od dataset")
print(df.head())

print("Dimension of diabetes dataset :", df.shape)

X_train, X_test, y_train, y_test = train_test_split(df.loc[:,df.columns != 'Outcome'],df['Outcome'],stratify = df['Outcome'], random_state = 33)

tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train,y_train)

print("Accuracy on training set : {:.3f}".format(tree.score(X_train,y_train)))
print("Accuracy on test set : {:.3f}".format(tree.score(X_test,y_test)))

tree = DecisionTreeClassifier(max_depth = 3, random_state = 0)
tree.fit(X_train,y_train)

print("Accuracy on training set : {:.3f}".format(tree.score(X_train,y_train)))
print("Accuracy on test set : {:.3f}".format(tree.score(X_test,y_test)))

print("Feature importance : \n{}".format(tree.feature_importances_))

def plot_feature_importance(model):
    plt.figure(figsize =(8,6))
    n_features = 8
    plt.barh(range(n_features), model.feature_importances_, align = 'center')
    diabetes_features = [x for i, x in enumerate(df.columns) if i !=8]
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel('Feature Importance')
    plt.ylabel('Features')
    plt.ylim(-1,n_features)
    plt.show()

plot_feature_importance(tree)
