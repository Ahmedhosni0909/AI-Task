#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:31:47 2022

@author: ahmed
"""
#import Lisb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

# Import dataset
dataset = pd.read_csv('diabetes.csv')

X = dataset.iloc[:, 0:8].values
X = pd.DataFrame(X)
Y = dataset.iloc[:, 8].values
Y = pd.DataFrame(Y)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=7)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)

clf = DecisionTreeClassifier().fit(X_train, Y_train)
Y_pred = clf.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)
print("Decision tree accuracy: "+ str(accuracy))

