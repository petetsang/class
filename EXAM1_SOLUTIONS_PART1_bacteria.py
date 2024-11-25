#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bacteria.py
# Python 3.7
"""
Created on Tue Mar 19 17:48:04 2019

@author: pedro brodude
Modified:  Tue Mar 19 17:48:04 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt



tau = 3.4
A = .06

t = np.linspace(0,13,100)

V = 1 - np.exp(-t/tau)
W = A* (np.exp(-t/tau)-1 + t/tau)




plt.plot(t, W, color='r',linestyle=':')

plt.plot(t, V, color='b')


data_novicka = np.loadtxt("PMLSdata/15novick/g149novickA.csv", delimiter=',')


x=data_novicka[:,0]

y = data_novicka[:,1]

plt.scatter(x,y)

data_novickb = np.loadtxt("PMLSdata/15novick/g149novickB.csv", delimiter=',')


x2 = data_novickb[:,0]
y2 = data_novickb[:,1]
plt.scatter(x2,y2)