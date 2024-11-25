#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Mon Mar 11 13:30:36 2019

@author: pedro brodude
Modified:  Mon Mar 11 13:30:36 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

import urllib

web_file = urllib.request.urlopen("https://cdiac.ess-dive.lbl.gov/ftp/trends/temp/vostok/vostok.1999.temp.dat")

data_set = np.loadtxt(web_file,skiprows=60)

years_bp = data_set[:,1]
temp_deg_c = data_set[:,3]

plt.scatter(years_bp,temp_deg_c)

# label axes
ax = plt.gca()



#ax.set_title("Vostok temp record",size=24, weight='bold')
ax.set_xlabel("years_before_present")

ax.set_ylabel("Relative temperature in degrees Celsius")
plt.title('Ice core temperature record from Vostok', pad=10)

plt.savefig("vostok_temp.svg")