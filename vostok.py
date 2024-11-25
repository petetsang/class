#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Mar 15 14:38:40 2019

@author: pedro brodude
Modified:  Fri Mar 15 14:38:40 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt



import urllib

web_file = urllib.request.urlopen("https://cdiac.ess-dive.lbl.gov/ftp/trends/temp/vostok/vostok.1999.temp.dat")

#data_set = np.loadtxt(web_file,comments='*',skiprows=60)
 
data_set = np.loadtxt(web_file,skiprows=60)


years_bp = data_set[:,1]

temp = data_set[:,3]



plt.scatter(years_bp,temp, label="Vostok Ice Core Temp")



# label Title, Axis, Legend
ax = plt.gca()
ax.set_title("Vostok", size=24, weight='bold')
ax.set_xlabel("years before present(before Jan 1st, 1950)")
ax.set_ylabel("Temperature change in degrees Celsius")
ax.legend()

#
##label Title, axis, legend  II
#
#plt.scatter(  years_bp, temp,   label="vostok ice core temp"   )
#
#
#plt.title("Vostok temperature record", size=24, weight='bold')
#plt.xlabel("Years Before Present (years before Jan 1st, 1950)")
#plt.ylabel("Temperature change in Celsius degrees")
#plt.legend()