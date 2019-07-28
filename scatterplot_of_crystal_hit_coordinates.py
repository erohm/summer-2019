from root_numpy import root2array, tree2array, tree2rec
import pprint
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from collections import Counter 
import time 

''' Below measures computation time '''
start_time = time.time()

''' First get the TTree from the ROOT file '''
import ROOT
rfile = ROOT.TFile('muons_100_evts.root')
intree = rfile.Get('qtree')

''' This list 'array' will hold the values from the root file, and is nested. Element array[i][1] holds event number for event 1. Element array[i]  '''
array = tree2rec(intree)

fig = pyplot.figure()
ax = Axes3D(fig)

i=0
event_coords = [[] for j in range(0,9)]

plt.figure()
while array[i][1] == array[i+1][1]:
	event_coords[i].extend([array[i][11], array[i][12], array[i][13]])
	ax.scatter(xs=array[i][11], ys=array[i][12], zs=array[i][13])
	i+= 1
#print(event_coords)
plt.show()

'''
event_coords[1].extend([1,2,3])
print(event_coords[1][1])
'''
