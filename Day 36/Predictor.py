import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

def PlayPredictor(data_path,values):
    df = pd.read_csv(data_path)

    print("Size of Dataset :", df.shape)
    print("Columns :", df.columns)

    features = df[['Whether','Temperature']]

    le = LabelEncoder()

    def label_encoder(df):
        encoded_df = df.copy()
        for col in df.columns:
            if df[col].dtype == 'objcet':
                encoded_df[col] = le.fit_transform(df[col])

        return encoded_df
    
    encoded_df = label_encoder(features)

    print("endoced:",encoded_df)
    label = le.fit_transform(df['Play'])

    KNN_model = KNeighborsClassifier(n_neighbors = 3)
    KNN_model.fit(encoded_df,label)

    inputs = le.transform(values)
    Predicted = KNN_model.predict(inputs)
    return Predicted

def Inputs(W,T):
    if W not in range(4) or T not in range(4):
        print("Invalid input")
        exit()
    else:
        wether_dict = {1:'Overcast',2:'Rainy',3:'Sunny'}
        temp_dict = {1:'Hot',2:'Cold',3:'Mild'}
        result = [wether_dict[W],temp_dict[T]]

    return result

def main():
    print("Play Predictor Application")
    print("Choose the current whether between 1.Overcast 2.Rainy 3.Sunny")
    W = int(input("Wether option :"))

    print("Choose the current Temperature between 1.Hot 2.Cold 3.Mild")
    T = int(input("Temperature option :"))

    values = Inputs(W,T)
    
    result =PlayPredictor("PlayPredictor.csv",values)
    print(result)

if __name__=="__main__":
    main()
