# -*- coding: utf-8 -*-
"""codeshastra.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c99kGqvXFRvt7_UH5IGGCL8fem0HJHvj
"""


import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

import pickle

import matplotlib.pyplot as plt

future = []

def read_file(filename):
  #file name should contain relative path
  data2 = pd.read_csv(filename)#'./MARUTI_data.csv'
  data = data2.values
  return data

def preprocess(data):
  #dates = data[:, 0]
  X = np.array(list(data[:, 1:]), dtype=np.float) # took 1 hour bug
  mask = ~np.isnan(X).any(axis=1)
  X = X[mask] #took 1 hr to find the bug
  data = data[mask]
  #print(X.shape, data.shape)
  X = X[:, 3] #working on close
  #X_train = X_train.reshape(-1, 1)
  #X_train = X[0:3000]
  #X_test = X[3001:]
  #X_test.shape
  return X# , dates #whole of train

#X_train
 

def scaling(X_train):
  X_train = X_train.reshape(-1, 1)
  sc = MinMaxScaler(feature_range = (0, 1))
  training_set_scaled = sc.fit_transform(X_train)
  return training_set_scaled, sc

def train(training_set_scaled):
  X_train = []
  y_train = []
  for i in range(60, 3000):
      X_train.append(training_set_scaled[i-60:i, 0])
      y_train.append(training_set_scaled[i, 0])
  X_train, y_train = np.array(X_train), np.array(y_train)

  X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
  return X_train, y_train

def tr_model(X_train, y_train):
  # Initialising the RNN
  regressor = Sequential()

  # Adding the first LSTM layer and some Dropout regularisation
  regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
  regressor.add(Dropout(0.2))

  # Adding a second LSTM layer and some Dropout regularisation
  regressor.add(LSTM(units = 50, return_sequences = True))
  regressor.add(Dropout(0.2))

  # Adding a third LSTM layer and some Dropout regularisation
  regressor.add(LSTM(units = 50, return_sequences = True))
  regressor.add(Dropout(0.2))

  # Adding a fourth LSTM layer and some Dropout regularisation
  regressor.add(LSTM(units = 50))
  regressor.add(Dropout(0.2))

  # Adding the output layer
  regressor.add(Dense(units = 1))

  # Compiling the RNN
  regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
  return regressor
  # Fitting the RNN to the Training set

#def actual_training(regressor):
#  regressor.fit(X_train, y_train, epochs = 1, batch_size = 32)
#  return regressor

def store_model(regressor, filename):
  pickle.dump(regressor, open(filename, 'wb'))
  return True

#files.download(filename)

def load_model(filename):
  reg = pickle.load(open(filename, 'rb'))
  return reg

def test_sol(X, sc, regressor):
  #X_t = X_test.reshape((-1, 1))
  #print(X_t.shape)
  var = X.reshape((-1, 1))
  #print(var.shape)
  #np.concatenate((X_train, X_test.reshape(-1, 1)), axis = 0) 
  inputs = sc.transform(var)

  X_test = []
  #print(inputs.shape)
  for i in range(60, inputs.shape[0]):
    X_test.append(inputs[i-60:i, 0])
  
  X_test = np.array(X_test)
  #print("X_test.shape ", X_test.shape)
  #X_test.shape
  X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
  #print(X_test)
  #for i in range(0, 60):
  #  print(X_test[0][i], X_test[1][i])
  predicted_stock_price = regressor.predict(X_test)
  predicted_stock_price = sc.inverse_transform(predicted_stock_price)

  return predicted_stock_price #X is real stock prices
# %matplotlib inline

def perpetual(count, X, sc, regressor):
  '''
  X should be shaped as 1, 60, 1
  '''
  for i in range(count):
    #print(X)
    #var = X_test = X.reshape((-1, 1)) #60, 1
    inputs = sc.transform(X)
    X_test = np.array(inputs)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    predicted_stock_price = regressor.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)
    print("predicted: ", predicted_stock_price)
    future.append(predicted_stock_price[0, 0])
    X = np.roll(X, -1)
    X[0, 59] = predicted_stock_price[0, 0]
    #print(X)
    
  

def plotit(real_stock_price, predicted_stock_price):
  #real_stock_price = X
  plt.plot(real_stock_price, color = 'red', label = 'Real Google Stock Price')
  plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Google Stock Price')
  plt.title('Google Stock Price Prediction')
  plt.xlabel('Time')
  plt.ylabel('Google Stock Price')
  plt.legend()
  plt.show()

filename = 'model.pkl'
X = read_file('/home/hemal/Desktop/codeshastra/HISTORICAL_DATA/3IINFOTECH_data.csv')
X_train, dates = preprocess(X)
training_set_scaled, sc = scaling(X_train)
#X_train,y_train = train(training_set_scaled)
#regressor = tr_model(X_train, y_train)
#regressor = actual_training(regressor)
#store_model(regressor, filename)
regressor = load_model('hundred_epochs.pkl')
predicted_stock_price = test_sol(X_train, sc, regressor)
real_stock_price = X_train


#perpetual()

A = real_stock_price.reshape(-1, 1)
temp = A[-60:].reshape(1, 60)
#print(temp)
perpetual(60, temp, sc, regressor)
F = np.array(future)
F = F.reshape(F.shape[0], 1)
B = predicted_stock_price.reshape(-1, 1)
B = np.concatenate((B, F), axis=0)
#for i, j in zip(A, B):
#  print(i, j)
# from datetime import datetime  
# from datetime import timedelta 
# date = datetime.strptime(dates[-1], '%Y-%m-%d')
# print(date)
plotit(A, B)