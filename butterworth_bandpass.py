from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np


# import sampling rate and time stamp from noise_signal module
from noise_signal import t, my_signal

# Critcal Frequencies
lowcut = 200
highcut = 700

def band_butter(sig, time, crit_low, crit_high, order):
    
    # sampling frequency
    Fs = len(time)/max(time)
    
    # nyquist frequency 
    Fn = 0.5*Fs 
    
    # normalize critical frequencies
    low = lowcut/Fn 
    high = highcut/Fn
    
    # filter coefficients
    b,a = signal.butter(order,[low,high],btype='band')

    # filtered signal
    sig_filt = signal.lfilter(b,a,sig)
    
    # frequency response
    w,h = signal.freqz(b,a,worN=2000)
    
    # Plots
    style.use('ggplot')
    style.use('dark_background')
    
    plt.title('Filter Frequency Response')
    plt.plot((Fs*0.5/np.pi)*w, abs(h),label = f'order={order}', color = 'orange')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.grid()
    plt.legend(loc='best')

    f,plt_arr= plt.subplots(2,sharex=True)
    
    plt_arr[0].plot(time, sig, color ='red')
    plt_arr[0].set_title('Input Signal', color ='red')
    plt_arr[0].set_ylabel('Amplitude')
     
    plt_arr[1].plot(time, sig_filt,color='cyan')
    plt_arr[1].set_title('Filtered Signal', color ='cyan')
    plt_arr[1].set_ylabel('Amplitude')
    plt_arr[1].set_xlabel('time (seconds)')
   
    plt.show()
    
band_butter(my_signal, t, lowcut, highcut, 6)