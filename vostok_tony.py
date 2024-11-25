#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Mar 15 14:36:38 2019

@author: pedro brodude
Modified:  Fri Mar 15 14:36:38 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

import urllib



web_file = urllib.request.urlopen("https://cdiac.ess-dive.lbl.gov/ftp/trends/temp/vostok/vostok.1999.temp.dat")

data = web_file.readlines()



data2 =  list(map(lambda x: x.decode("utf-8"), data[60:])) 



depth = np.asarray(list(map(lambda x: x[:4].strip(), data2)),

                   dtype = int)

age = np.asarray(list(map(lambda x: x[5:15].strip(), data2)),

                   dtype = int)

content = np.asarray(list(map(lambda x: x[16:26].strip(), data2)),

                   dtype = float)

temp = np.asarray(list(map(lambda x: x[-7:-2].strip(), data2)),

                   dtype = float)

                  

vostok_ice = np.vstack((depth,age,content,temp)).T