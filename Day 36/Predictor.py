import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

def PlayPredictor(data_path,values):
    df = pd.read_csv(data_path)
    inputs = pd.DataFrame({'Whether':[values[0]],'Temperature':[values[1]]})

    whether_encoder = LabelEncoder()
    df['whether_encoded'] = whether_encoder.fit_transform(df['Whether'])

    tem_encoder = LabelEncoder()
    df['temp_encoded'] = tem_encoder.fit_transform(df['Temperature'])

    labels = LabelEncoder()
    df['Target']=labels.fit_transform(df['Play'])

    X = df[['whether_encoded','temp_encoded']]
    y = df['Target']


    KNN_model = KNeighborsClassifier(n_neighbors = 3)
    KNN_model.fit(X,y)

    inputs['whether_encoded']=whether_encoder.transform(inputs['Whether'])
    inputs['temp_encoded']=tem_encoder.transform(inputs['Temperature'])

    Predicted = KNN_model.predict(inputs[['whether_encoded','temp_encoded']])
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
    
    if result[0]==1:
        print("Yes, you can play")
    elif result[0]==0:
        print("No, yo cant play")

if __name__=="__main__":
    main()
