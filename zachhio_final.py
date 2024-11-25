import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng
num_flips=1000
p=.08
time=np.arange(1,num_flips+1)
flips=rng(num_flips)
heads=(flips<p)
string=heads*1
a=np.nonzero(string)
wait_time_diff=np.diff(a)
wait_time=wait_time_diff.flatten()
b=93
times=np.arange(1,b+1)
plt.scatter(times,wait_time)