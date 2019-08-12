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
'''
f=open("ChannelPosition.txt", "r")

list=[]
f1 = f.readlines()
for x in f1:
	list.append(x)
print(list[5])
print(list[6])
print(list[6][0])
 list[6][0] returns "7", the crystal number. Need to pay attention not to get an off by one error 
print(list[0])
print(list[0][5])

list = [[] for j in range(0,987)]

with open('ChannelPosition.txt') as f:
    data = f.read().splitlines()
    data = [i.split() for i in data if any(j.isdigit() for j in i)]
    for i in data:
        print('Crystal: {}\nx: {}\ny: {}\nz: {}'.format(i[0], i[1], i[2], i[3]))
        print("==================================")
        list[i].extend([i[1], i[2], i[3]])
        ax.scatter(xs=i[1], ys=i[2], zs=i[3])
print(list)
plt.show()
'''
data = np.loadtxt('ChannelPosition.dat')
#print(data[0][0])
print(data[0][0])
''' NEXT: create a dictionary (or even a list) with these values, the keys being crystal number, holding x, y, z values. Then figure out how to plot the coordinates. ''' 
















	
