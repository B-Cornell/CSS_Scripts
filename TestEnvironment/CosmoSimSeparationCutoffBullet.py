import numpy as np
import matplotlib.pyplot as plt
import math

row_id45, rockstarId45, snapnum45, x45, y45, z45, vx45, vy45, vz45, Mvir45, Rvir45, depthFirstId45, mainLeaf_depthFirstId45 = np.loadtxt('CSVFiles/BigMDPL_6E13_Snap_45.csv', delimiter = ',', unpack = True, skiprows = 1)
f = open('reduced_cosmo_pairs_bullet.txt', 'w')
def sep(i,j):
    separation = math.sqrt( ((x45[i]-x45[j])*(x45[i]-x45[j])) + ((y45[i]-y45[j])*(y45[i]-y45[j])) + ((z45[i]-z45[j])*(z45[i]-z45[j])))
    return separation
k = 1
print "Loaded up..."
snap48 = []
for i in range(len(row_id45)):

    if snapnum45[i] == 48:
        snap48.append(i)

print "Array of length " + str(len(snap48)) + " created..."


for k in range(len(snap48)):
    print float(k)/float(len(snap48))
    j = k + 1
    while(x45[snap48[j]] < x45[snap48[k]]+5):
        if (sep(snap48[k],snap48[j]) < 5) :
            if rockstarId45[snap48[k]] != rockstarId45[snap48[j]]:
                f.write( str(snap48[k]) +'\n')
                f.write( str(rockstarId45[snap48[k]]) + ',' + str(snapnum45[snap48[k]]) + ',' + str(Mvir45[snap48[k]]) + ',' + str(Rvir45[snap48[k]]) + ',' + str(depthFirstId45[snap48[k]]) + ',' + str(mainLeaf_depthFirstId45[snap48[k]]) + ',' + str(x45[snap48[k]]) + ', ' + str(y45[snap48[k]]) + ', ' + str(z45[snap48[k]]) + ', ' + str(vx45[snap48[k]]) + ', ' + str(vy45[snap48[k]]) + ', ' + str(vz45[snap48[k]])+'\n')
                f.write( str(rockstarId45[snap48[j]]) + ',' + str(snapnum45[snap48[j]]) + ',' + str(Mvir45[snap48[j]]) + ',' + str(Rvir45[snap48[j]]) + ',' + str(depthFirstId45[snap48[j]]) + ',' + str(mainLeaf_depthFirstId45[snap48[j]]) + ',' + str(x45[snap48[j]]) + ', ' + str(y45[snap48[j]]) + ', ' + str(z45[snap48[j]]) + ', ' + str(vx45[snap48[j]]) + ', ' + str(vy45[snap48[j]]) + ', ' + str(vz45[snap48[j]])+'\n')
                k = k+1
        j=j+1
