#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Tue Apr  2 13:18:59 2019

@author: pedro brodude
Modified:  Tue Apr  2 13:18:59 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

# streamlines.py

lower, upper, step = -2, 2, 0.1

coords = np.arange(lower, upper + step, step)

X, Y = np.meshgrid(coords, coords)

#Vx, Vy = Y ,  -X
#Vx = Y - 0.1 * X

#Vy = -X - 0.1 * Y
Vx, Vy = X , -Y

plt.streamplot(X, Y, Vx, Vy, linewidth=2)