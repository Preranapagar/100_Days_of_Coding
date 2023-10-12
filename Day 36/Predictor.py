import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

def PlayPredictor(data_path,values):
    df = pd.read_csv(data_path)

    print("Size of Dataset :", df.shape)
    print("Columns :", df.columns)

    le = LabelEncoder()

    whether_en = le.fit_transform(df['Whether'])
    temp_en = le.fit_transform(df['Temperature'])
    label = le.fit_transform(df['Play'])

    features = list(zip(whether_en,temp_en))

    KNN_model = KNeighborsClassifier(n_neighbors = 3)
    KNN_model.fit(features,label)

    Predicted = KNN_model.predict(values)
    return Predicted

def Inputs(W,T):
    wether_dict = {1:'Overcast',2:'Rainy',3:'Sunny'}
    temp_dict = {1:'Hot',2:'Cold',3:'Mild'}

    result = [wether_dict[W],temp_dict[T]]

    return result

def main():
    print("Play Predictor Application")
    print("Choose the current whether between 1.Overcast 2.Rainy 3.Sunny")
    W = int(input("Wether option"))

    print("Choose the current Temperature between 1.Hot 2.Cold 3.Mild")
    T = int(input("Temperature option"))

    values = Inputs(W,T)

if __name__=="__main__":
    main()
