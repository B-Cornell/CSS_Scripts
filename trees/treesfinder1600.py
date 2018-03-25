import numpy as np
import math
number1 = 1600
number2 = number1+100
#unpack the final data so that we can get the relevant rockstar ids
pairid, rockstarida, rockstaridb, massa, massb, radiusa, radiusb, mainleafa, mainleafb, depthfirsta, depthfirstb, separation, vel_on, vel_off = np.loadtxt('realmainleafdfids.csv', delimiter = ',', unpack = True)

#unpack the trees
treefilestring = 'Trees_sn68_m6e13_'+str(number1)+'_'+str(number2)+'.csv'
trowid, trockstar, tsnapnum, tx, ty, tz, tvx, tvy, tvz, tmass, trad, tdepthfirstid = np.loadtxt(treefilestring, delimiter = ',', skiprows = 1, unpack = True)



minx = float(number1)/2500.
maxx = float(number2)/2500.

minx = minx * 82248
maxx = maxx * 82248


f = open("treefile_"+str(number1)+".csv", "w")
later = open("late_treefile_"+str(number1)+".csv", "w")

def sepvel(hax, hay, haz, hbx, hby, hbz, avx, avy, avz, bvx, bvy, bvz):
	if (avx != 0 and avy != 0 and avz != 0 and bvx != 0 and bvy != 0 and bvz != 0 and hax != 0 and hay != 0 and haz != 0 and hbx != 0 and hby != 0 and hbz != 0):
		x = hax - hbx
		y = hay - hby
		z = haz - hbz
		vx = avx - bvx
		vy = avy - bvy
		vz = avz - bvz
		position = math.sqrt((x*x)+(y*y)+(z*z))
		velocity = math.sqrt(vx**2+vy**2+vz**2)
		Vel_par = ((vx)*(x)+(vy)*(y)+(vz)*(z))/position
		Vel_perp = math.sqrt((velocity*velocity)-(Vel_par*Vel_par))
		return position, Vel_par, Vel_perp
	else: 
		return 100, 100000, 100000
		 
	
    
    
    
for i in range(int(minx),int(maxx)): #cyclethrough every pair in the final data set
	
	postfinder = [[0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0]] 
	
	j = -1 
	written = False
	p = 0
	haloa = rockstarida[i]
	halob = rockstaridb[i]
	
    
	for k in range(len(trowid)):
		if (tdepthfirstid[k] < mainleafa[i] and tdepthfirstid[k] > depthfirsta[i]):
			postfinder[int(tsnapnum[k]-69)][6] = tvx[k]
			postfinder[int(tsnapnum[k]-69)][7] = tvy[k]
			postfinder[int(tsnapnum[k]-69)][8] = tvz[k]
			postfinder[int(tsnapnum[k]-69)][0] = tx[k]
			postfinder[int(tsnapnum[k]-69)][1] = ty[k]
			postfinder[int(tsnapnum[k]-69)][2] = tz[k]
		elif(tdepthfirstid[k] < mainleafb[i] and tdepthfirstid[k] > depthfirstb[i]):
			postfinder[int(tsnapnum[k]-69)][9] = tvx[k]
			postfinder[int(tsnapnum[k]-69)][10] = tvy[k]
			postfinder[int(tsnapnum[k]-69)][11] = tvz[k]
			postfinder[int(tsnapnum[k]-69)][3] = tx[k]
			postfinder[int(tsnapnum[k]-69)][4] = ty[k]
			postfinder[int(tsnapnum[k]-69)][5] = tz[k]
			
	smallest = 100
	onvelarr = [0]*10
	offvelarr = [0]*10
	separr = [0] * 10
	while(p < len(postfinder)):
		pairsep, paironvel, pairoffvel = sepvel(*postfinder[p])
		separr[p] = pairsep
		onvelarr[p] = paironvel 
		offvelarr[p] = pairoffvel
		if pairsep < 5:
			print str(p+69) + ', ' + str(pairsep)
		if (pairsep < smallest):
			smallest = pairsep
			passsnap = p
			onvelsnap = paironvel
			offvelsnap = pairoffvel
			
		p += 1
	if smallest < .7:
	   
		string = str(pairid[i]) + ', ' + str(rockstarida[i]) + ', ' + str(rockstaridb[i]) + ', ' + str(massa[i]) + ', ' + str(massb[i]) + ', ' + str(radiusa[i]) + ', ' + str(radiusb[i]) + ', ' + str(separation[i]) + ', ' + str(vel_on[i]) + ', ' + str(vel_off[i]) + ', ' + str(passsnap+69) + ', ' + str(smallest) + ', ' + str(onvelsnap) + ', ' + str(offvelsnap)
		f.write(string)            
		f.write('\n')
		print string
		latedata = str(pairid[i]) + ', ' + str(rockstarida[i]) + ', ' + str(rockstaridb[i]) + ', ' + str(massa[i]) + ', ' + str(massb[i]) + ', ' + str(radiusa[i]) + ', ' + str(radiusb[i]) + ', ' + str(separr[0]) + ', ' + str(onvelarr[0]) + ', ' + str(offvelarr[0]) + ', ' + str(separr[1]) + ', ' + str(onvelarr[1]) + ', ' + str(offvelarr[1]) + ', ' + str(separr[2]) + ', ' + str(onvelarr[2]) + ', ' + str(offvelarr[2]) + ', ' + str(separr[3]) + ', ' + str(onvelarr[3]) + ', ' + str(offvelarr[3]) + ', ' + str(separr[4]) + ', ' + str(onvelarr[4]) + ', ' + str(offvelarr[4]) + ', ' + str(separr[5]) + ', ' + str(onvelarr[5]) + ', ' + str(offvelarr[5]) + ', ' + str(separr[6]) + ', ' + str(onvelarr[6]) + ', ' + str(offvelarr[6]) + ', ' + str(separr[7]) + ', ' + str(onvelarr[7]) + ', ' + str(offvelarr[7]) + ', ' + str(separr[8]) + ', ' + str(onvelarr[8]) + ', ' + str(offvelarr[8]) + ', ' + str(separr[9]) + ', ' + str(onvelarr[9]) + ', ' + str(offvelarr[9]) + ', ' + str(separation[i])  + ', ' + str(vel_on[i]) + ', ' + str(vel_off[i])
		
		later.write(latedata)
		later.write('\n')
		print latedata
            
            

