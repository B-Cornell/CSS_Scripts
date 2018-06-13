#This finds all the pairs within 5Mpc of eachother in our data

import numpy as np
import matplotlib.pyplot as plt
import math
import sys

#function that finds 3D separation of two halos given two indices. Only works after declaring arrays named x, y, and z
def sep(i,j):
    separation = math.sqrt( ((x[i]-x[j])*(x[i]-x[j])) + ((y[i]-y[j])*(y[i]-y[j])) + ((z[i]-z[j])*(z[i]-z[j])))
    return separation
k = 1


#get which snapshot is wanted based on user input in terminal
snapshot = int(sys.argv[1])


#finding which CSV file to find the appropriate snapshots in. They are broken up into groups of either
#5 or 10, so if we want snap 32, we want CSVFiles/BigMDPL_6E13_Snap_30.csv since that is where the halos
# at snapshot 32 are kept
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

#unpacking the correct CSV file based on the tilenum variable we find earlier. This is where we get the x, y, and z
# arrays that correspond to the positions of each of the halos and later use to find close halo pairs
row_id, rockstarId, snapnum, x, y, z, vx, vy, vz, Mvir, Rvir, depthFirstId, mainLeaf_depthFirstId = np.loadtxt('CSVFiles/BigMDPL_6E13_Snap_'+str(tilenum)+'.csv', delimiter = ',', unpack = True, skiprows = 1)


#open a file to write the data
f = open('reduced_cosmo_pairs_increased_timeframe_' + str(snapshot) + '.txt', 'w')



# loop through the CSV file to find all the halos at the snapshot we are interested in and then saves the indice
# to the snap array. This allows us to filter out all the extraneous halos
snap = []
for i in range(len(row_id)):
    if snapnum[i] == snapshot:
        snap.append(i)

#just see how much data we have to go through
print "Array of length " + str(len(snap)) + " created..."


#-------Below this is where all the real computation time is----------

#loop through all the halos in the relevant snapshot. Have to call everything as array[snap[k]] since snap[k]
#is the actual indice of the CSV files, not k. We have to do range(len(snap)) instead of just snap because
#we want to check all the next values in the current time step, so we have to step by 1 through snap, not
#not through the CSV arrays
for k in range(len(snap)):

    #this just prints the progress
    if k%500 == 0:
        print float(k)/float(len(snap)) * 100

    #when we loop through, we only check for pairs of each halo after the current indice and at the right snap
    #this prevents double counting pairs and cuts runtime significantly
    j = k + 1

    #this loops through the CSV file and stops checking once the halos are 5Mpc away in x from our current halo
    #We can do this since we are only interested in pairs less than 5Mpc apart in 3D.
    while(x[snap[j]] < x[snap[k]]+5):

        #Saves the data if the halos are less than 5Mpc apart
        if (sep(snap[k],snap[j]) < 5) :
            #double check we aren't using two of the same halo
            if rockstarId[snap[k]] != rockstarId[snap[j]]:
                #write out the relevant information for both halos in the pair
                f.write( str(snap[k]) +'\n')
                f.write( str(rockstarId[snap[k]]) + ' ' + str(snapnum[snap[k]]) + ' ' + str(Mvir[snap[k]]) + ' ' + str(Rvir[snap[k]]) + ' ' + str(depthFirstId[snap[k]]) + ' ' + str(mainLeaf_depthFirstId[snap[k]]) + ' ' + str(x[snap[k]]) + ', ' + str(y[snap[k]]) + ', ' + str(z[snap[k]]) + ', ' + str(vx[snap[k]]) + ', ' + str(vy[snap[k]]) + ', ' + str(vz[snap[k]])+'\n')
                f.write( str(rockstarId[snap[j]]) + ' ' + str(snapnum[snap[j]]) + ' ' + str(Mvir[snap[j]]) + ' ' + str(Rvir[snap[j]]) + ' ' + str(depthFirstId[snap[j]]) + ' ' + str(mainLeaf_depthFirstId[snap[j]]) + ' ' + str(x[snap[j]]) + ', ' + str(y[snap[j]]) + ', ' + str(z[snap[j]]) + ', ' + str(vx[snap[j]]) + ', ' + str(vy[snap[j]]) + ', ' + str(vz[snap[j]])+'\n')
        #increment j to continue loop
        j=j+1
