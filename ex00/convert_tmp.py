import scipy.io as sio
import matplotlib.pyplot as  plt
import numpy as n
import h5py

# Read auroral ionization rate data
d=sio.loadmat("A_ionization4JV20240112.mat")
height_km=d["h"][0]

eb=300
t_idx=200
# production
# 
# use values  between
# 10 and 20 kEv
q=d["dE"][0,eb]*d["Ie"][eb,t_idx]*d["A"][:,eb]

# ionization rate per cubic meter for a single electron per square meter
q=3e10*q/n.max(q)/1e12/1.34

ho=h5py.File("q_10keV.h5","w")
# ionizations per cubic meter per second for an incident electron per squaremeter per second. (1/(m^5 * s^2))
ho["q"]=q
ho["hgt"]=height_km
ho["energy"]=d["Ec"][0][eb]
ho.close()

