#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:04:48 2022

@author: ahmed
"""
#import libs
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

# Import  dataset
dataset = pd.read_csv('diabetes.csv')

x = dataset.iloc[:, 0:8].values
x = pd.DataFrame(x)
y = dataset.iloc[:, 8].values
y = pd.DataFrame(y)


x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=7)

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)

KNN = KNeighborsClassifier().fit(x_train,y_train.values.ravel())
y_pred = KNN.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print("KNN Accuracy: "+ str(accuracy))











