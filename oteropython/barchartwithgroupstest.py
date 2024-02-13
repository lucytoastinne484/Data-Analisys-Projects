
import matplotlib.pyplot as plt
import numpy as np

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

import matplotlib.pyplot as plt

#a program to exibit the grouped bar with labels#

#first we need to identify the groups we need analyze#

groups_data = pd.read_csv(r"C:\Users\Computador\oteropython\abcgorups.csv")
plt.title("Groups data")


companies = ("CompanyA","CompanyB","CompanyC")

profit_by_region = ({
    'Region A':(1000.0,1000.0,2500.0),
    'Region B':(1599.8,1000.0,2300.0),
    'Region C':(189.95, 195.82, 217.19),
    
    
    })

x = np.arrange(len(companies))
width = 0.25
multiply_by = 0

fig,ax = plt.subplot(layout='constrained')

for region,profit in  profit_by_region.items():
    offset = width * multiply_by
    chart = ax.bar(x + offset,profit,width,label=region)
    ax.bar_label(chart,padding = 3) #labels of each group#
    multiply_by +=1
    
    ax.set_ylabel('Length (mm)')
    ax.set_title('Penguin attributes by species')
    ax.set_xticks(x + width, companies)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 250)
plt.legend()


plt.show()