#this goes through all the pairs and finds the tree history of both halos in the pair

import numpy as np
import math
import sys

#get the snapshot from the terminal input
redshift = int(sys.argv[1])
print redshift

#unpack the corresponding file
pairid, pairaindex, pairbindex, pairamvir, pairbmvir, pairar200b, pairbr200b,  pairamainleaf,  pairbmainleaf,  pairadepthfirst,  pairbdepthfirst,  pairbposz, pairbvelz, pairbvely = np.loadtxt('UniquePairData/separation_data_increased_timeframe' + str(redshift) + '.csv', delimiter = ',', unpack = True, skiprows = 1)

#create the array we're saving all the data in filled with 0s
#structure is [ [0,0,0,0,0,[0,0,0,...0,0,0]], [0,0,0,0,0,[0,0,0,...0,0,0]], ...]
#             [ [pair data,[tree data at all snapshots]],
treehistorydata = [[0,0,0,0,0,[0]*(3*(redshift-9))] for x in range(len(pairid))]

#fill in the initial pair data for each pair
for i in range(len(pairid)):
    treehistorydata[i][0] = pairamvir[i]
    treehistorydata[i][1] = pairbmvir[i]
    treehistorydata[i][2] = pairbposz[i]
    treehistorydata[i][3] = pairbvelz[i]
    treehistorydata[i][4] = pairbvely[i]


#cycle through every snapshot before the current one
for snapshot in range(9,redshift):
    print snapshot

    #unpack the data in that timestep
    snapid, snapaindex, snapbindex, snapamvir, snapbmvir, snapar200b, snapbr200b,  snapamainleaf,  snapbmainleaf,  snapadepthfirst,  snapbdepthfirst,  snapbposz, snapbvelz, snapbvely = np.loadtxt('UniquePairData/separation_data_increased_timeframe' + str(snapshot) + '.csv', delimiter = ',', unpack = True, skiprows = 1)

    #cycle through all the pairs in our catalog looking for trees in this snapshot
    for i in range(len(pairid)):
        j = 0

        #tag to stop looping once we find the tree
        quicker = False

        #percentage tracker
        if i%500 == 0:
            print float(i)/float(len(pairid))

        #loop through all the treedata to find the tree
        while j < len(snapid) and quicker == False:
            # if the main leafs match, its a tree and we save the data to our data array and flag it to exit the loop
            if (pairamainleaf[i] == snapamainleaf[j] and pairbmainleaf[i] == snapbmainleaf[j]) or (pairbmainleaf[i] == snapamainleaf[j] and pairamainleaf[i] == snapbmainleaf[j]):
                treehistorydata[i][5][(snapshot-9)*3] = snapbposz[j]
                treehistorydata[i][5][((snapshot-9)*3)+1] = snapbvelz[j]
                treehistorydata[i][5][((snapshot-9)*3)+2] = snapbvely[j]
                quicker = True
            j += 1

#open the save file to write the data
f=open('full_tree_data_'+str(redshift)+'.txt', 'w')

#writing all the data into the file in a useable format
for i in range(len(treehistorydata)):
    datastring = ''
    for j in range(3*(redshift-9)):
        datastring = datastring + ', ' + str(treehistorydata[i][5][j])
    f.write(str(treehistorydata[i][0]) + ', ' + str(treehistorydata[i][1]) + ', ' + str(treehistorydata[i][2]) + ', ' + str(treehistorydata[i][3]) + ', ' + str(treehistorydata[i][4]) + datastring + '\n')
