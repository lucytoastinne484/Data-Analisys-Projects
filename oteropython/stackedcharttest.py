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



samples =  (
    "Cobalt\n 0.66g per ml",
    "Niquel\n 3.09g per ml",
    "Carbon\n 6.02g per ml",
)

composition_percentage = {
    "Iron":nm.array([12.0,20.0,12.1]),
    "Diamond":nm.array([9.99,6.78,11.45])
    }

wid = 0.5

fig, ax = plt.subplots()

bottom =nm.zeros(3)

for x, y in composition_percentage.items():
    p = ax.bar(samples,y,wid,label=x,bottom=bottom)
    bottom += y
    
ax.set_title("Composition of each element by g/ml")
ax.legend(loc="upper right")

plt.show()
