import numpy as np
import math
#unpack the final data so that we can get the relevant rockstar ids
pairid, rockstarida, rockstaridb, massa, massb, radiusa, radiusb, mainleafa, mainleafb, depthfirsta, depthfirstb, separation, vel_off, vel_on = np.loadtxt('realmainleafdfids.csv', delimiter = ',', unpack = True)

#unpack the trees
trowid, trockstar, tsnapnum, tx, ty, tz, tvx, tvy, tvz, tmass, trad, tdepthfirstid = np.loadtxt('trees/Trees_sn68_m6e13_1100_1200.csv', delimiter = ',', skiprows = 1, unpack = True)


f = open("treefile_1100_1200.csv", "w")

def sep(hax, hay, haz, hbx, hby, hbz):
	if (hax != 0 and hay != 0 and haz != 0 and hbx != 0 and hby != 0 and hbz != 0):
		xab = hax - hbx
		yab = hay - hby
		zab = haz - hbz
		totalsep = math.sqrt(xab**2 + yab**2 + zab**2)
		return totalsep
	else:
		return 100
		

	
    
    
    
    
    
for i in range(37000,42500): #cyclethrough every pair in the final data set
	print i
	postfinder = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]] 
	j = -1 
	written = False
	p = 0
	haloa = rockstarida[i]
	halob = rockstaridb[i]
	
	if i % 200 == 0: 
	    r = (float(i)/float(len(pairid))) *100
	    print '                                  ' + str(r)
            
    
	for k in range(len(trowid)):
		if (tdepthfirstid[k] < mainleafa[i] and tdepthfirstid[k] > depthfirsta[i]) or (tdepthfirstid[k] < mainleafb[i] and tdepthfirstid[k] > depthfirstb[i]):
            
			if (tdepthfirstid[k] < mainleafa[i] and tdepthfirstid[k] > depthfirsta[i]):
				postfinder[int(tsnapnum[k]-69)][0] = tx[k]
				postfinder[int(tsnapnum[k]-69)][1] = ty[k]
				postfinder[int(tsnapnum[k]-69)][2] = tz[k]
			else:
				postfinder[int(tsnapnum[k]-69)][3] = tx[k]
				postfinder[int(tsnapnum[k]-69)][4] = ty[k]
				postfinder[int(tsnapnum[k]-69)][5] = tz[k]
	
	while(p < len(postfinder) and written == False):
		
		if (sep(*postfinder[p]) < .35):   
			string = str(pairid[i]) + ',' + str(rockstarida[i]) + ',' + str(rockstaridb[i]) + ',' + str(massa[i]) + ',' + str(massb[i]) + ',' + str(radiusa[i]) + ',' + str(radiusb[i]) + ',' + str(separation[i]) + ',' + str(vel_off[i]) + ',' + str(vel_on[i])
			f.write(string)            
			f.write('\n')
			written = True
		p += 1
            
            

