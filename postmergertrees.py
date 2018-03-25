import numpy as np
import math

pairid, rockstara, rockstarb, massa, massb, radiusa, radiusb, separation, vel_z, vel_y, passsnap, lowsep, passvel_z, passvel_y = np.loadtxt('trees/treefile.csv', delimiter = ',', unpack = True)

f = open("trees/treefilepostmerger.csv", "w")
haba = 0
for a in range(len(pairid)):
	if (separation[a] > lowsep[a]) or (separation[a] < lowsep[a] and vel_z[a] > 0):
		f.write(str(pairid[a]) + ', ' + str(rockstara[a]) + ', ' + str(rockstarb[a]) + ', ' + str(massa[a]) + ', ' + str(massb[a]) + ', ' + str(radiusa[a]) + ', ' + str(radiusb[a]) + ', ' + str(separation[a]) + ', ' + str(vel_z[a]) + ', ' + str(vel_y[a]) + ', ' + str(passsnap[a]) + ', ' + str(lowsep[a]) + ', ' + str(passvel_z[a]) + ', ' + str(passvel_y[a]) + '\n')
		haba += 1
f.close()
print haba
print len(pairid)

