#!/usr/bin/env python3

import numpy as n
# plotting
import matplotlib.pyplot as plt
# reader for hdf5 files
import h5py

# read example meteor head echo event
h=h5py.File("example_meteor.h5","r")
# epoch (unix seconds)
t_epoch=h["t_epoch"][()]
# time in seconds relative to epoch
t=h["t"][()]
# east-west position as a function of time in meters
east=h["east_meters"][()]
# north-south position as a function of time in meters
north=h["north_meters"][()]
# up position as a function of time in meters
up=h["up_meters"][()]

# note that all positions are relative to observer-centric east-north-up coordinate system
# centered at the MAARSY radar antenna center at Andenes, Norway

# signal-to-noise ratio for the object. The noise bandwidth is 31.25 kHz
# assuming perfect pulse compression for a 16 bit complementary code with 2 microsecond
# transmit bits.
snr=h["snr"][()]

# number of measurements
n_meas=len(east)

plt.subplot(221)
plt.plot(t,east,".",label="Measurement")
plt.ylabel("East-West (m)")
plt.xlabel("Time since epoch (s)")
plt.legend()

plt.subplot(222)
plt.plot(t,north,".",label="Measurement")
plt.ylabel("North-South (m)")
plt.xlabel("Time since epoch (s)")

plt.subplot(223)
plt.plot(t,up,".",label="Measurement")
plt.ylabel("Up (m)")
plt.xlabel("Time since epoch (s)")

plt.subplot(224)
plt.plot(t,10.0*n.log10(snr),".")
plt.ylabel("Signal-to-noise ratio (dB)")
plt.xlabel("Time since epoch (s)")
plt.tight_layout()
plt.show()
h.close()


