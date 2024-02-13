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

array = ([200,30,70,90])
values_label = ["Notebboks","pens","ruler","eraser"]
explode_pie = [0.1,0.1,0.1,0.1]
color = ['r','y','g','c']
plt.pie(array,
        labels=values_label,
        startangle=270,
        explode=explode_pie,
        shadow=True,
        colors=color
        )
plt.legend(title="School material")
plt.show()