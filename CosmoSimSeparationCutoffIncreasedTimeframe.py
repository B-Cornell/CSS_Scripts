import numpy as np
import matplotlib.pyplot as plt
import math
import sys

def sep(i,j):
    separation = math.sqrt( ((x[i]-x[j])*(x[i]-x[j])) + ((y[i]-y[j])*(y[i]-y[j])) + ((z[i]-z[j])*(z[i]-z[j])))
    return separation
k = 1


snapshot = int(sys.argv[1])
snap = []
if snapshot > 0:
    if snapshot < 10:
        tilenum = 0
    elif snapshot < 20:
        tilenum = 10
    elif snapshot < 30:
        tilenum = 20
    elif snapshot < 35:
        tilenum = 30
    elif snapshot < 40:
        tilenum = 35
    elif snapshot < 45:
        tilenum = 40
    elif snapshot < 50:
        tilenum = 45
    elif snapshot < 55:
        tilenum = 50
    elif snapshot < 60:
        tilenum = 55
    elif snapshot < 65:
        tilenum = 60
    elif snapshot < 70:
        tilenum = 65
    else:
        tilenum = 70
row_id, rockstarId, snapnum, x, y, z, vx, vy, vz, Mvir, Rvir, depthFirstId, mainLeaf_depthFirstId = np.loadtxt('CSVFiles/BigMDPL_6E13_Snap_'+str(tilenum)+'.csv', delimiter = ',', unpack = True, skiprows = 1)
f = open('reduced_cosmo_pairs_increased_timeframe_' + str(snapshot) + '.txt', 'w')

for i in range(len(row_id)):

    if snapnum[i] == snapshot:
        snap.append(i)

print "Array of length " + str(len(snap)) + " created..."


for k in range(len(snap)):
    if k%500 == 0:
        print float(k)/float(len(snap)) * 100
    j = k + 1
    while(x[snap[j]] < x[snap[k]]+5):
        if (sep(snap[k],snap[j]) < 5) :
            if rockstarId[snap[k]] != rockstarId[snap[j]]:
                f.write( str(snap[k]) +'\n')
                f.write( str(rockstarId[snap[k]]) + ' ' + str(snapnum[snap[k]]) + ' ' + str(Mvir[snap[k]]) + ' ' + str(Rvir[snap[k]]) + ' ' + str(depthFirstId[snap[k]]) + ' ' + str(mainLeaf_depthFirstId[snap[k]]) + ' ' + str(x[snap[k]]) + ', ' + str(y[snap[k]]) + ', ' + str(z[snap[k]]) + ', ' + str(vx[snap[k]]) + ', ' + str(vy[snap[k]]) + ', ' + str(vz[snap[k]])+'\n')
                f.write( str(rockstarId[snap[j]]) + ' ' + str(snapnum[snap[j]]) + ' ' + str(Mvir[snap[j]]) + ' ' + str(Rvir[snap[j]]) + ' ' + str(depthFirstId[snap[j]]) + ' ' + str(mainLeaf_depthFirstId[snap[j]]) + ' ' + str(x[snap[j]]) + ', ' + str(y[snap[j]]) + ', ' + str(z[snap[j]]) + ', ' + str(vx[snap[j]]) + ', ' + str(vy[snap[j]]) + ', ' + str(vz[snap[j]])+'\n')
                k = k+1
        j=j+1
