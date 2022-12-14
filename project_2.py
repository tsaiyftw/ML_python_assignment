# -*- coding: utf-8 -*-
"""project_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r0Lqfz8UuQztFltlYLOW6jsc1T72PNoS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

train_data = pd.read_csv("/content/drive/MyDrive/Colab_Notebooks/project_2/train.csv")
test_data= pd.read_csv("/content/drive/MyDrive/Colab_Notebooks/project_2/test.csv")
test_id = test_data["PassengerId"]
train_data

train_data.describe()

print(len(train_data.loc[train_data["HomePlanet"]=="Europa"]))
print(len(train_data.loc[train_data["HomePlanet"]=="Earth"]))
print(len(train_data.loc[train_data["HomePlanet"]=="Mars"]))
2131+4602+1759

print(len(train_data.loc[train_data["CryoSleep"]==True]))
print(len(train_data.loc[train_data["CryoSleep"]==False]))
3037+5439

print(len(train_data.loc[train_data["Destination"]=="TRAPPIST-1e"]))
print(len(train_data.loc[train_data["Destination"]=="PSO J318.5-22"]))
print(len(train_data.loc[train_data["Destination"]=="55 Cancri e"]))
5915+796+1800

print(len(train_data.loc[train_data["VIP"]==True]))
print(len(train_data.loc[train_data["VIP"]==False]))
199+8291

def clean(data):
  data.Cabin.fillna("F/3/P",inplace=True)
  data.HomePlanet.fillna("Earth",inplace=True)
  data.CryoSleep.fillna(False,inplace=True)
  data.Destination.fillna("TRAPPIST-1e",inplace=True)
  data.VIP.fillna(False, inplace=True)

  data = data.drop(["PassengerId","Cabin","Name"], axis=1)

  cols = ["Age","RoomService","FoodCourt","ShoppingMall","Spa","VRDeck"]
  for col in cols:
    data[col].fillna(data[col].mean(), inplace=True)

  return data

train_data = clean(train_data)
test_data = clean(test_data)
train_data.head(17)

X = train_data.iloc[:,:-1]
Y = train_data.iloc[:, -1:].values.ravel()
print(f"train x shape: {X.shape}")
print(f"train y shape: {Y.shape}")
print(f"test x shape: {test_data.shape}")

dummy_x = pd.get_dummies(X)
print(dummy_x.shape)
dummy_x

from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
x_scaled = scaler.fit_transform(dummy_x)
x_scaled

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

depth = []
for i in range(2,100,1):
  rf = RandomForestClassifier(max_depth=i)
  scores = cross_val_score(rf,x_scaled,Y, cv=5)
  depth.append(scores.mean())

final_depth = np.argmax(np.array(depth))+2
print(final_depth)

estimators =[]
for i in tqdm(range(50,200,1)):
  rf = RandomForestClassifier(n_estimators=i, max_depth=final_depth)
  scores = cross_val_score(rf,x_scaled,Y,cv=5)
  estimators.append(scores.mean())

final_estimator = np.argmax(np.array(estimators)) +50
print(final_estimator)

final_rf = RandomForestClassifier(n_estimators= final_estimator, max_depth=final_depth)
final_rf.fit(x_scaled, Y)

dummy_test_data= pd.get_dummies(test_data)
test_data_x_scaled = scaler.transform(dummy_test_data)
y_predicted = final_rf.predict(test_data_x_scaled)
print(y_predicted)

submission_data = pd.DataFrame({"PassengerId":test_id.values, "Transported": y_predicted})
submission_data.to_csv("submission.csv",index=False)