import matplotlib as plt
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

#country = ['Brazil', 'Germany','USA','Russia']
#gdp = [45000,46000,80000,70000]

#plt.bar(country,gdp)
#plt.xlabel('Countries')
#plt.ylabel('GDP per capita')
#plt.show()#

extract_data = pd.read_csv(r"C:\Users\Computador\Documents\fictcionalcompaniesavgprofit.csv")
companies = extract_data["Company"]
avg_profit = extract_data["AVG profit"]

plt.bar(companies,avg_profit)
plt.xlabel('Company')
plt.ylabel('AVG Profit in R$')
plt.title("Company avg profit")
plt.show()

