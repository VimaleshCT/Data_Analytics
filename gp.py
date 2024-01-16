import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

df =pd.read_csv("gld_price_data.csv")
df.head()

x=df['SPX','USO','SLV','EUR/USD']
Y=df['GLD']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
scaler  = MinMaxScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model= Sequential

model.add(Dense(10,activation='relu',input_dim=4))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='linear'))

model.compile(loss='mean_squared_error',optimizer='Adam')

history = model.fix(x_train_scaled,y_train,epochs=50,validation_split=0.1)

y_pred =model.predict(x_test_scaled)

from sklearn.metrics import r2_score

r2_score(y_test,y_pred)
