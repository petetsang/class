import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 40.0, 0.001)
a0 = 1
tau = 1
delta_f = .1
s = 1-a0*np.exp((-t)/tau)
l, = plt.plot(t, s, lw=2, color='red')
plt.axis([0, 15, 0, 1])




###### [START] data scatter plot

data_novicka = np.loadtxt("PMLSdata/15novick/g149novickA.csv", delimiter=',')


x=data_novicka[:,0]

y = data_novicka[:,1]

plt.scatter(x,y)


##### [END] of data scatter plot




axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'tau', 0, 10.0, valinit=f0, valstep=delta_f)
samp = Slider(axamp, 'Amp', 0., 10.0, valinit=a0)


def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(1-amp*np.exp((freq**(-1))*(-t)))
    fig.canvas.draw_idle()
sfreq.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()

