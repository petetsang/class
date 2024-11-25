import numpy as np
import matplotlib.pyplot as plt


time = np.linspace(0, 10 , 101)

time 


# assign variables

B = 0

A = 100000

alpha = 10

beta = 0.5

viral_load = A * np.exp(-alpha*time) + B * np.exp(-beta*time)



plt.plot(time, viral_load)



#hiv_data = np.loadtxt("data/HIVseries.csv",delimiter=',')
#time_in_days = hiv_data[:,0]
#concentration = hiv_data[:,1]

hiv_data = np.load("PMLSdata/01HIVseries/HIVseries.npz")
concentration = hiv_data['viral_load']
time_in_days = hiv_data['time_in_days']


plt.plot(time_in_days,concentration,'+', markersize=20)


# labeling and embelishments

ax = plt.gca()
ax.set_title("title here")
ax.set_xlabel("time in days")
ax.legend(["legend1","legend2"])