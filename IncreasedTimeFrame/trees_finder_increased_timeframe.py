import numpy as np
import math
number1 = 00
number2 = number1+100
#unpack the final data so that we can get the relevant rockstar ids
pairid, rockstarida, rockstaridb, massa, massb, radiusa, radiusb, mainleafa, mainleafb, depthfirsta, depthfirstb, separation, vel_on, vel_off = np.loadtxt('separation_data_increased_timeframe.csv', delimiter = ',', unpack = True, skiprows = 1)

#unpack the trees
filearray = [0,10,20,30,35,40,45,50,55,60,65,70]
percentagecounter = 0
f = open("treefile_increased_timeframe.csv", "w")
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


for file in filearray:

	treefilestring = 'CSVFiles/BigMDPL_6E13_Snap_'+str(file)+'.csv'
	print treefilestring

	trowid, trockstar, tsnapnum, tx, ty, tz, tvx, tvy, tvz, tmass, trad, tdepthfirstid, tmainleaf = np.loadtxt(treefilestring, delimiter = ',', skiprows = 1, unpack = True)
	print 'Loaded..............' + str(file)

	for i in range(1000):#len(pairid)):
		#cyclethrough every pair in the final data set
		if float(i)%500 == 0:
			print (((float(i)/float(len(pairid))))/(float(len(filearray)))) + (float(percentagecounter)/(float(len(filearray))))

		for k in range(1000):#len(trowid)):
			if (tmainleaf[k] == mainleafa[i]) or (tmainleaf[k] == mainleafb[i]):
				f.write(str(trowid[k]) + ', ' + str(trockstar[k]) + ', ' + str(tsnapnum[k]) + ', ' + str(tx[k]) + ', ' + str(ty[k]) + ', ' + str(tz[k]) + ', ' + str(tvx[k]) + ', ' + str(tvy[k]) + ', ' + str(tvz[k]) + ', ' + str(tmass[k]) + ', ' + str(trad[k]) + ', ' + str(tdepthfirstid[k]) + ', ' + str(tmainleaf[k]) + '\n')





	percentagecounter +=1
