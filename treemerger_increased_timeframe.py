import numpy as np
import math
import sys

#trowid, trockstar, tsnapnum, tx, ty, tz, tvx, tvy, tvz, tmass, trad, tdepthfirstid, tmainleaf = np.loadtxt('treefile_bullet.csv', delimiter = ',', unpack = True)

#pairid, pairaindex, pairbindex, pairamvir, pairbmvir, pairar200b, pairbr200b, pairamainleaf, pairbmainleaf, pairadepthfirst, pairbdepthfirst, pairbposz, pairbvelz, pairbvely = np.loadtxt('bullet_separation_data.csv', delimiter = ',', unpack = True)


#f = open('mainplustrees_increased_timeframe.txt', 'w')
#                   mass, mass, sep, velz, vely, 3*snaps
redshift = int(sys.argv[1])
print redshift
pairid, pairaindex, pairbindex, pairamvir, pairbmvir, pairar200b, pairbr200b,  pairamainleaf,  pairbmainleaf,  pairadepthfirst,  pairbdepthfirst,  pairbposz, pairbvelz, pairbvely = np.loadtxt('UniquePairData/separation_data_increased_timeframe' + str(redshift) + '.csv', delimiter = ',', unpack = True, skiprows = 1)
treehistorydata = [[0,0,0,0,0,[0]*(3*(redshift-9))] for x in range(len(pairid))]

for i in range(len(pairid)):
    treehistorydata[i][0] = pairamvir[i]
    treehistorydata[i][1] = pairbmvir[i]
    treehistorydata[i][2] = pairbposz[i]
    treehistorydata[i][3] = pairbvelz[i]
    treehistorydata[i][4] = pairbvely[i]



for snapshot in range(9,redshift):
    print snapshot
    snapid, snapaindex, snapbindex, snapamvir, snapbmvir, snapar200b, snapbr200b,  snapamainleaf,  snapbmainleaf,  snapadepthfirst,  snapbdepthfirst,  snapbposz, snapbvelz, snapbvely = np.loadtxt('UniquePairData/separation_data_increased_timeframe' + str(snapshot) + '.csv', delimiter = ',', unpack = True, skiprows = 1)
    for i in range(len(pairid)):
        j = 0
        quicker = False
        if i%500 == 0:
            print float(i)/float(len(pairid))
        while j < len(snapid) and quicker == False:
            if (pairamainleaf[i] == snapamainleaf[j] and pairbmainleaf[i] == snapbmainleaf[j]) or (pairbmainleaf[i] == snapamainleaf[j] and pairamainleaf[i] == snapbmainleaf[j]):
                treehistorydata[i][5][(snapshot-9)*3] = snapbposz[j]
                treehistorydata[i][5][((snapshot-9)*3)+1] = snapbvelz[j]
                treehistorydata[i][5][((snapshot-9)*3)+2] = snapbvely[j]
                quicker = True
            j += 1

f=open('full_tree_data_'+str(redshift)+'.txt', 'w')


for i in range(len(treehistorydata)):
    datastring = ''
    for j in range(3*(redshift-9)):
        datastring = datastring + ', ' + str(treehistorydata[i][5][j])
    f.write(str(treehistorydata[i][0]) + ', ' + str(treehistorydata[i][1]) + ', ' + str(treehistorydata[i][2]) + ', ' + str(treehistorydata[i][3]) + ', ' + str(treehistorydata[i][4]) + datastring + '\n')
