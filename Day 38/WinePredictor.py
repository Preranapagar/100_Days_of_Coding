import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def WinePredictor(df):
    print("Shape of Dataset :", df.shape)
  
    


def main():
    print("Wine Predictor Application")
    
    data = pd.read_csv("WinePredictor.csv")
    
    WinePredictor(data)


if __name__=="__main__":
    main()
