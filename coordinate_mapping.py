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

coordinates = np.loadtxt('ChannelPosition.dat')
#print(coordinates[0][0])

plt.figure()
for i in range (0,988):
	print(coordinates[i][0],": ", coordinates[i][1], ", ", coordinates[i][2], ", ", coordinates[i][3])
	ax.scatter(xs=coordinates[i][1], ys=coordinates[i][2], zs=coordinates[i][3], color='b')
plt.show()
	
''' The ith crystal number coordinates are contained in the (i+1)th element of the list '''
















	
