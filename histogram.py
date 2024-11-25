#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Mon Mar 18 14:53:18 2019

@author: pedro brodude
Modified:  Mon Mar 18 14:53:18 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

from numpy.random import random as rng

data = rng(100)

plt.hist(data, bins=10,align='left')