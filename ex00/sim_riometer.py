import h5py
import matplotlib.pyplot as plt
import numpy as n
import scipy.interpolate as sinterp
import scipy.integrate as sinteg


# Precomputed ionization profile using Sergienko and Ivanov (1993)
# 
h=h5py.File("q_10keV.h5","r")
# ionization rate as a function of altitude of a
# precipitation flux of one electron per squaremeter per second
# primary auroral electron with energy of 10 keV
q=h["q"][()]
# height in meters
hgt=h["hgt"][()]*1e3
# energy of primary precipitating electron
E=h["energy"][()]
h.close()

# E-region recombination coefficient (Brekke)
recombination_coeff=3e-13

# plot ionization rate
plt.semilogx(q,hgt/1e3)
plt.title("Ionization-rate $q(h)$\n(for an incident flux of 1 m$^{-2}$s$^{-1}$ precipitating electrons)")
plt.xlabel("Ionization rate (m$^{-3}$ s$^{-1}$)")
plt.ylabel("Height (km)")
plt.tight_layout()
plt.show()

# altitude step in meters
dh=n.diff(hgt)[0]

# total number of ionizations per second per incident primary electron
# (should be about 300 for a 10 keV electron, source: Björn)
Q_tot=sinteg.trapezoid(q,hgt,dx=dh)

# steady state electron density
plt.semilogx(n.sqrt(1e12*q/recombination_coeff),hgt/1e3)
plt.title("Steady-state electron density $n_e(h) = \\sqrt{q(h)/\\alpha}$")
plt.xlabel("Electron density ($m^{-3}$)")
plt.ylabel("Height (km)")
plt.show()

