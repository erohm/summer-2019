from root_numpy import root2array, tree2array, tree2rec
import pprint
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# First get the TTree from the ROOT file
import ROOT
rfile = ROOT.TFile('muons_10k_evts.root')
intree = rfile.Get('qtree')

array = tree2rec(intree)

event = 1
i = 0
mult = []

while i < len(array)-1:
	if array[i][1] == event:
		mult.append(array[i][1])
# This block takes care of the last iterable element of a given event number before going to the next event
	elif array[i+1][1] != event:
		mult.append(array[i][1])
	event += 1
	i += 1

# Sets data points to be evenly spaced 
xbins = np.linspace(start=0, stop=10000, num = 51)
plt.hist(mult, bins=xbins) 
plt.show()


