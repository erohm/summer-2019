from root_numpy import root2array, tree2array, tree2rec
import pprint
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from collections import Counter 
import time 

''' Below measures computation time '''
start_time = time.time()

''' First get the TTree from the ROOT file '''
import ROOT
rfile = ROOT.TFile('pions_1k_evts_g4cuore.root')
intree = rfile.Get('outTree')

''' This list 'array' will hold the values from the root file, and is nested '''
array = tree2rec(intree)

# list[start:end:step] 
# end index is NOT inclusive
''' Block below creates a list called 'event_list' which contains all the event numbers in order and includes all duplicates. The list will look like [1, 1, 1, ... ... 1000, 10000] '''

i=0
event_list = []
while i < len(array):
	event_list.append(array[i][1])
	i += 1
print(array[0])
''' The following block creates a new list 'mult' containing the number of times an event number is repeated. Element i will say how many times event number j is repeated. A histogram of this will show the multiplicity of event numbers. If len(mult) is not the number of events you created in qshields, then you will know there has been a problem. '''

element = 0
j = 1
mult = []
while element < len(event_list):
	if j < max(event_list)+1:
		mult.append(event_list.count(j))
	else:
		break
	element+=1
	j+=1
#print(len(mult))

# Sets data points to be evenly spaced 
xbins = np.linspace(start=0, stop=6, num =6)
plt.hist(mult, bins=xbins)		 
plt.title('Multiplicity of Crystals Activated')
plt.xlabel('Number of Crystals Activated per Given Event')
plt.ylabel('Frequency of Activation')
plt.show()

''' Print computation time (because it seems to take a while and I want to know what variables affect this) '''
print("Computation time: " , time.time() - start_time, "s, or ", (time.time() - start_time)/60, "min" )










