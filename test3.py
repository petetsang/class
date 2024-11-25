#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri May  3 14:58:59 2019

@author: pedro brodude
Modified:  Fri May  3 14:58:59 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,10,100)
y = np.sin(x)*np.exp(x)+2*np.sin(x)*np.exp(x)+3+np.sin(x)*np.exp(x)+4+np.sin(x)*np.exp(x)+6*np.sin(x)*np.exp(x)


a=str(y)
plt.text(0,0,a)