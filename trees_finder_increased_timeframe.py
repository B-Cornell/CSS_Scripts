import numpy as np
import math
number1 = 00
number2 = number1+100
#unpack the final data so that we can get the relevant rockstar ids
pairid, rockstarida, rockstaridb, massa, massb, radiusa, radiusb, mainleafa, mainleafb, depthfirsta, depthfirstb, separation, vel_on, vel_off = np.loadtxt('separation_data_increased_timeframe.csv', delimiter = ',', unpack = True, skiprows = 1)

#unpack the trees

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

	for eachsnapnumber in range(10,20):
		arrayofsnaps = []
		for whatever in range(len(trowid)):
			if tsnapnum[whatever] == eachsnapnumber:
				arrayofsnaps.append([trockstar[whatever],tsnapnum[whatever],tx[whatever],ty[whatever],tz[whatever],tvx[whatever],tvy[whatever],tvz[whatever],tmass[whatever],trad[whatever],tdepthfirstid[whatever],tmainleaf[whatever]])

		for i in range(len(pairid)):
			#cyclethrough every pair in the final data set
			if float(i)%500 == 0:
				print (((float(i)/float(len(pairid))))/(float(len(filearray)))) + (float(percentagecounter)/(float(len(filearray))))

			for k in range(len(arrayofsnaps)):
				if (arrayofsnaps[k][11] == mainleafa[i]) or (arrayofsnaps[k][11] == mainleafb[i]):
					f.write(str(arrayofsnaps[k][0]) + ', ' + str(arrayofsnaps[k][1]) + ', ' + str(arrayofsnaps[k][2]) + ', ' + str(arrayofsnaps[k][3]) + ', ' + str(arrayofsnaps[k][4]) + ', ' + str(arrayofsnaps[k][5]) + ', ' + str(arrayofsnaps[k][6]) + ', ' + str(arrayofsnaps[k][7]) + ', ' + str(arrayofsnaps[k][8]) + ', ' + str(arrayofsnaps[k][9]) + ', ' + str(arrayofsnaps[k][10]) + ', ' + str(arrayofsnaps[k][11]) + '\n')




	percentagecounter +=1
