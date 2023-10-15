import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings 
warnings.filterwarnings('ignore')

def WinePredictor(df,inputs):

    Features = df.drop(['Class'],axis=1)
    label = df['Class']

    x_train, x_test, y_train, y_test = train_test_split(Features, label, test_size =0.3, random_state =34)

    classifier = KNeighborsClassifier(n_neighbors = 3)
    classifier.fit(x_train,y_train)

    values = pd.DataFrame(inputs)
    prediction = classifier.predict(values)

    return prediction

def CheckAccuracy(df,n):

    Features = df.drop(['Class'],axis=1)
    label = df['Class']

    x_train, x_test, y_train, y_test = train_test_split(Features, label, test_size =0.3, random_state =34)

    classifier = KNeighborsClassifier(n_neighbors = n)
    classifier.fit(x_train,y_train)

    prediction = classifier.predict(x_test)
    accuracy = accuracy_score(prediction,y_test)

    return accuracy



def main():
    print("Wine Predictor Application")
    
    data = pd.read_csv("WinePredictor.csv")

    observations = [[14.38,1.87,2.38,12,102,3.3,3.64,0.29,2.96,7.5,1.2,3,1547]]
    Class = WinePredictor(data, observations)

    print("Predicted Class of given data :", Class[0])
    neighbors = int(input("Enter the number of neighbors to check accuracy of model :"))
    Accuracy =CheckAccuracy(data,neighbors)
    print("Accuracy of model is :", Accuracy*100,"%")


if __name__=="__main__":
    main()
