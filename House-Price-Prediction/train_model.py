import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("dataset/train.csv")

print(df.head())

features = ["BedroomAbvGr", "FullBath", "KitchenAbvGr", "TotRmsAbvGrd", "LotArea", "GarageArea", "Neighborhood"]  
target = "SalePrice"

le = LabelEncoder()
df["Neighborhood"] = le.fit_transform(df["Neighborhood"])

X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "house_price_model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("Model and label encoder saved successfully!")
