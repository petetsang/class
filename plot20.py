#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Tue Mar  5 13:10:40 2019

@author: pedro brodude
Modified:  Tue Mar  5 13:10:40 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

num_points = 5

x_min , x_max = 0, 4
x_values = np.linspace(x_min,x_max,num_points)

y_values = x_values**2

plt.plot(x_values,y_values)