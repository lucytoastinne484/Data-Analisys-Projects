import csv as comma
import pandas as pd
import os as OS
import sys as system
import matplotlib as matplot


import matplotlib.pyplot as plt

import matplotlib.dates as md

import matplotlib.ticker as MaxNLocator

import math as calculate

import matplotlib_inline as mt_inline

import pandas as pd

import numpy as nm

#r=to start we use pandas to extract our file
raw_data = pd.read_csv(r"C:\Users\Computador\Downloads\car data all together.csv")

#linear chart, this is the viz we select#

plt.xticks(range(0,len(raw_data["price"])),raw_data["CarName"],rotation=90)
#then we use the rows to represent the values showed#
convertible = raw_data[raw_data['carbody'] == 'convertible'].reset_index()#then we aregoing to organize this viz#
#and we ajust the size #
plt.title("Convertible cars")
plt.figure(figsize=(15,10))#size adjust#
plt.plot(convertible["price"])
plt.xticks(range(0,len(convertible["price"])),convertible["CarName"],rotation=90)
plt.show()
plt.clf()
# the we are gonna do the same process but for the carbodies#
#carbodies= raw_data['carbody'].unique()
#for body in carbodies:
   # plt.title(body,fontsize=20)
    #convertible = raw_data[raw_data['carbody'] == body ].reset_index()
   # plt.figure(figsize=(20,1))
   # plt.plot(raw_data["price"])
   # plt.xticks(range(0,len(convertible["price"])),convertible["CarName"],rotation=90)#
    

    
    

    