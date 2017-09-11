import numpy as np
import math
#unpack the final data so that we can get the relevant rockstar ids
pairid, rockstarida, rockstaridb, massa, massb, radiusa, radiusb, separation, vel_off, vel_on= np.loadtxt('uniquedata.csv', delimiter = ',', unpack = True)

#unpack the first cosmo data set so that we can get the main leaf and depthfirst ids of each of the halos in
rowid, haloid, x, y, z, vx, vy, vz, mvir, rvir, mainleaf, depthfirst  = np.loadtxt('BigMDPL_6e13_X_depthfirstId.csv', delimiter = ',', unpack = True)

f = open("realmainleafdfids.csv", "w")

for i in range(len(pairid)): #cyclethrough every pair in the final data set
	mainleafa = 0
	mainleafb = 0
	j = -1 
	written = False
	p = 0
	haloa = rockstarida[i]
	halob = rockstaridb[i]
	
	if i % 200 == 0: 
	    r = (float(i)/float(len(pairid))) * 100
	    print '                                  ' + str(r)
	   
	    
	while ( mainleafa == 0 or mainleafb == 0):
		j +=1
		if haloid[j] == haloa:
			mainleafa = mainleaf[j]
			depthfirsta = depthfirst[j]
			

		if haloid[j] == halob:
			mainleafb = mainleaf[j]
			depthfirstb = depthfirst[j]
	f.write(str(pairid[i]) + ', ' + str(rockstarida[i]) + ', ' + str(rockstaridb[i]) + ', ' + str(massa[i]) + ', ' + str(massb[i]) + ', ' + str(radiusa[i]) + ', ' + str(radiusb[i]) + ', ' + str(mainleafa) + ', ' + str(mainleafb) + ', ' + str(depthfirsta) + ', ' + str(depthfirstb) + ', ' + str(separation[i]) + ', ' + str(vel_off[i]) + ', ' + str(vel_on[i])+'\n')
