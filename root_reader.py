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

# and convert the TTree into an array
#array = tree2array(intree)

array = tree2rec(intree)
#print("Total Entries: ", len(array))
#for i in range(0, 749):
#   print("Entry: ", i+1)
#    print(" --> ", "Time: ", array[i][0])

pprint.pprint(dir(array[0]))
#print(type(array))
#for event in range(0,1001):
#    print("Event: ", event+1, ", X: ", array[event][12], ", Y: ", array[event][13], ", Z: ", array[event][14])
#print(array.dtype.names)

fig = pyplot.figure()
ax = Axes3D(fig)

# Making lists for the coordinates of crystals
x = [] # element 12
y = [] # element 13
z = [] # element 14
event = 1
# array[i][1] is where the value of event "i" is stored
#for i in range(0,20):
#	if array[i][1] == event:
#		ax.scatter(xs=array[event][12], ys=array[event][13], zs=array[event][14])
#		print("Event: ", event)
#		print("---------------------------------")
#		print(array[event][12], array[event][13], array[event][14])
#		i += 1
#	else:
#		event += 1
#plt.show()
#plt.figure()
#        print(coords)
# in this loop, plot the list contents 
# print(array[i][1]    
plt.figure()
i = 0
while i < len(array)-1:
	if array[i][1] == event:
#		print("Event: ", array[i][1])
#		print("X: ",array[i][12],", Y: ",array[i][13],", Z: ",array[i][14])
		ax.scatter(xs=array[event][12], ys=array[event][13], zs=array[event][14])
# This block takes care of the last iterable element of a given event number before going to the next event	
	elif array[i+1][1] != event:
#		print("Event: ", array[i][1])
#		print("X: ",array[i][12],", Y: ",array[i][13],", Z: ",array[i][14])
		ax.scatter(xs=array[event][12], ys=array[event][13], zs=array[event][14])
	event += 1
	i += 1
plt.show()
plt.savefig("muons_10k_evts.png")
# All the activated crystals in a given event are showing the same x,y,z values. Why?


