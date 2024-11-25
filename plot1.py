#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Mar  1 13:37:02 2019

@author: pedro brodude
Modified:  Fri Mar  1 13:37:02 2019
Description
____________________

"""


import numpy as np
import matplotlib.pyplot as plt

# simple_plot.py

import numpy as np, matplotlib.pyplot as plt

num_points = 5

x_min, x_max = 0, 4

x_values = np.linspace(x_min, x_max, num_points)

y_values = x_values**2



assert len(x_values) == len(y_values), \
     "Length-mismatch: {:d} versus {:d}".format(len(x_values),len(y_values))



plt.plot(x_values, y_values, label="Population 1")

plt.plot(x_values, x_values**3, label="Population 2")

plt.legend()
# plt.show()

plt.savefig('class_graph.png')
ax = plt.gca()
ax.set_title("My first plot", size=24, weight='bold')
ax.set_xlabel("speed $\\mu$m")


lines = ax.get_lines()
plt.setp(lines[0], linestyle='--', linewidth=3, color='r')