#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:22:47 2021

@author: ahmed

"""
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np



#read the file
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()


# drop ALL duplicate values
dataset.drop_duplicates(subset =("Title","Company","Location","Type","Level","YearsExp","Country","Skills"),
					keep = "first", inplace = True)


#Count  jobs for each company
company = dataset.Company.value_counts().to_frame()
#pie chart
company[company.Company>10].plot(kind='pie',figsize=(15,10),subplots=True)
#bar chart
company[company.Company>10].plot(kind='bar',figsize=(15,10))



#most popular jobs titles.
jobs=dataset.Title.value_counts().to_frame()
#pie chart
jobs[jobs.Title>10].plot(kind='pie',figsize=(15,10),subplots=True)
#bar chart
jobs[jobs.Title>10].plot(kind='bar',figsize=(15,10))





#most popular job areas.
areas = dataset.Location.value_counts().to_frame()
#pie chart
areas[areas.Location>10].plot(kind='pie',figsize=(15,10),subplots=True)
#bar chart
areas[areas.Location>10].plot(kind='bar',figsize=(15,10))



#most required skills
skills = dataset.Skills.value_counts().to_frame()

