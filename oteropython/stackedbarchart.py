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

species = (
    "Adelie\n $\\mu=$3700.66g",
    "Chinstrap\n $\\mu=$3733.09g",
    "Gentoo\n $\\mu=5076.02g$",
)
weight_counts = {
    "Below": nm.array([70, 31, 58]),
    "Above": nm.array([82, 37, 66]),
}
width = 0.5

fig, ax = plt.subplots()
bottom = nm.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")

plt.show()