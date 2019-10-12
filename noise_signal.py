import numpy as np

# generate signal
fs =5000
T = 0.1
t = np.linspace(0.0,T,T*fs)

x1 = 0.11*np.sin(2*np.pi*0.89*np.sqrt(t)+0.65) # amp = 0.1 freq = 2.2
x2 = 0.03*np.sin(2*np.pi*150*t+0.2) # amp = 0.03 freq = 300
x3 = 0.015*np.sin(2*np.pi*600*t) # amp = 0.2 freq = 900
x4 = 0.015*np.sin(2*np.pi*2000*t) # amp = 0.2 freq = 900

my_signal = x1+x2+x3+x4
