#!/usr/bin/env python


import numpy as n
import h5py
import matplotlib.pyplot as plt
import scipy.interpolate as sinterp

# read measurements of power as a function of time and frequency on 2024-01-03
h=h5py.File("KIL_2024-01-03.h5","r")
h_qdc=h5py.File("KIL_QDC_2024-01-03.h5","r")
# print data keys
print(h.keys())

# power as a function of time and frequency
power=h["data"][()]
# frequencies used
freq=h["freq"][()]
time=h["timestamp"][()]

n_freq=len(freq)

# get smooth quiet day curve
# this will need to be interpolated
qdc=h_qdc["qdc_data"][()]

# seconds since midnight
t=h_qdc["t"][()]
t_interp=n.copy(t)
# adjust edges to ensure no edge effects seen in interpolation
t_interp[0]=t_interp[0]-1000
t_interp[-1]=t_interp[-1]+1000

plt.pcolormesh(t_interp,freq/1e6,qdc.T)
plt.title("Quiet day curve")
plt.xlabel("Time (seconds since midnight)")
plt.ylabel("Frequency (MHz)")
plt.show()

# sum O-mode and X-mode power together
power_total = power[:,0:n_freq] + power[:,n_freq:(2*n_freq)]

plt.pcolormesh(time,freq/1e6,10.0*n.log10(power_total.T))
cb=plt.colorbar()
cb.set_label("Power (dB)")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Time (seconds since midnight)")
plt.colorbar()
plt.show()

# TBD: estimate absorption
