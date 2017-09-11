import numpy as np
import matplotlib.pyplot as plt
import math

rowid, rockstarid, x, y, z, vx, vy, vz, mass, radius = np.loadtxt('BigMDPL_6E13_X_depthfirstId.csv', delimiter = ',', unpack = True)
f = open('reduced_cosmo_pairs.txt', 'w')
def sep(i,j):
    separation = math.sqrt( ((x[i]-x[j])*(x[i]-x[j])) + ((y[i]-y[j])*(y[i]-y[j])) + ((z[i]-z[j])*(z[i]-z[j])))
    return separation
k = 1

for i in range(889593):
    print i
    j = i + 1
    while(x[j] < x[i]+5):
        if (sep(i,j) < 5) :
            if rockstarid[i] != rockstarid[j]:
                f.write( str(k) +'\n')
                f.write( str(rockstarid[i]) + ',' + str(x[i]) + ', ' + str(y[i]) + ', ' + str(z[i]) + ', ' + str(vx[i]) + ', ' + str(vy[i]) + ', ' + str(vz[i]) + ', ' + str(mass[i]) + ', ' + str(radius[i]) +'\n')
                f.write( str(rockstarid[j]) + ',' + str(x[j]) + ', ' + str(y[j]) + ', ' + str(z[j]) + ', ' + str(vx[j]) + ', ' + str(vy[j]) + ', ' + str(vz[j]) + ', ' + str(mass[j]) + ', ' + str(radius[j]) +'\n')
                k = k+1
        j=j+1
            
            
            
            
            #866674
            #151657
