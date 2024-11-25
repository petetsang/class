#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Mon Apr  8 13:34:49 2019

@author: pedro brodude
Modified:  Mon Apr  8 13:34:49 2019
Description
____________________

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 5*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 5*np.pi, 128),
                    init_func=init, blit=True)
plt.show()
