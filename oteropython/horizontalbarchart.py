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

import matplotlib.pyplot as plt


barh_data = pd.read_csv(r"C:\Users\Computador\Documents\materialcost.csv")
plt.title("Material Revenue")
y = barh_data["item"]
x = barh_data["price"]
plt.xlabel("Revenue")
plt.ylabel("material")
plt.barh(y,x)
plt.plot()
plt.show()



