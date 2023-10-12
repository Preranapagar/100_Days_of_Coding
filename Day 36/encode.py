import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("PlayPredictor.csv")

features = df[['Whether','Temperature']]

le = LabelEncoder()

def Encoder(data):
    encoded_data = features.copy()

    for col in data.columns:
        if data[col].dtype == 'object':
            encoded_data[col] = le.fit_transform(data[col])

    return encoded_data

result = Encoder(features)

print(result)