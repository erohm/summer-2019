from root_numpy import root2array, tree2array, tree2rec
import pprint
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# First get the TTree from the ROOT file
import ROOT
rfile = ROOT.TFile('muons_100_evts.root')
intree = rfile.Get('qtree')

array = tree2rec(intree)

fig = pyplot.figure()
ax = Axes3D(fig)


i=0
# Loops over each entry in root file and plots each unique coordinate for all events. The index array[i][1] stores the ith event number here
# The elements array[event][12], array[event][13], array[event][14] hold the x,y,z values of the ith iteration of each event 


while array[i][1] == 8:
	print(array[i][11], array[i][12], array[i][13])
	ax.scatter(xs=array[i][11], ys=array[i][12], zs=array[i][13])
	i+=1
plt.show()
