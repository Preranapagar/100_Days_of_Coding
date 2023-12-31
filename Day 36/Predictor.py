import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def PlayPredictor(data,values):
    df = data
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
        temp_dict = {1:'Hot',2:'Cool',3:'Mild'}
        result = [wether_dict[W],temp_dict[T]]

    return result

def CheckAccuracy(data, k=3):
    df = data
    le = LabelEncoder()

    wether_encoded = le.fit_transform(df['Whether'])
    temp_encoded = le.fit_transform(df['Temperature'])
    target = le.fit_transform(df['Play'])

    Features = list(zip(wether_encoded,temp_encoded))

    X_train,X_test,y_train,y_test = train_test_split(Features,target,test_size=0.2, random_state = 33)

    model = KNeighborsClassifier(n_neighbors = k)
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracy = round(accuracy * 100,2)

    print(f"Accuracy score of model with {k} neighbors is {accuracy} %")
    


def main():
    print("Play Predictor Application")
    
    mode = int(input("Choose activity to perform between 1.PlayPredictor 2.AccuracyCheck :"))
    df = pd.read_csv("PlayPredictor.csv")
    
    if mode == 1:

        print("Choose the current whether between 1.Overcast 2.Rainy 3.Sunny")
        W = int(input("Wether option :"))

        print("Choose the current Temperature between 1.Hot 2.Cold 3.Mild")
        T = int(input("Temperature option :"))
        values = Inputs(W,T)
        
        result =PlayPredictor(df,values)
    
        if result[0]==1:
            print("Yes, you can play")
        elif result[0]==0:
            print("No, yo cant play")
    elif mode == 2:
        neighbors = int(input("Enter the number of neighbors :"))
        CheckAccuracy(df,neighbors)

    else:
        print("Invalid input")

if __name__=="__main__":
    main()
