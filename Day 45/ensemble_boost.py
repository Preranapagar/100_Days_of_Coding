#Ensemble machine learning application with boosting technique

#MNIST Case Study

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

iris = load_iris()
x = iris['data']
y = iris['target']

x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=56, test_size = 0.2)

abc = AdaBoostClassifier(n_estimators= 50, learning_rate =1)

model = abc.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("Accuracy :", accuracy_score(y_test, y_pred)*100,'%')