import numpy as np
import math
import matplotlib.pyplot as plt
import sys

generalmass, generalpericenter, individualclusters = False, False, False
for a in sys.argv:
	if a == 'mass':
		generalmass = True
for a in sys.argv:
	if a == 'pericenter':
		generalpericenter = True
for a in sys.argv:
	if a == 'clusters':
		individualclusters = True

print generalmass
print generalpericenter
print individualclusters



pairid, rockstara, rockstarb, massa, massb, radiusa, radiusb, separation, vel_z, vel_y, passsnap, lowsep, passvel_z, passvel_y = np.loadtxt('trees/treefilepostmerger.csv', delimiter = ',', unpack = True)

pericenterhistogram = []
#This lists all the inputs for each system
#Name, Separation, Separation Sigma, LOS Vel, LOS Vel Sigma, MassA, MassA Sigma, MassB, MassB Sigma]
musketball = ['Musketball', 1.0, .14, 670, 330, 3.1E14, 1.2E14, 1.7E14, 2.0E14]
ciza = ['Ciza', 1.3, .13, 69, 190, 11E14, 3.7E14, 9.8E14, 3.8E14]
rxcj1314 = ['RXCJ1314', .54, .23, 1523, 149, 6.07E14, 1.8E14, 7.17E14, 2.8E14]
bullet = ['Bullet', .72, .025, 616, 80, 15E14, 1.5E14, 1.5E14, .15E14]
bulletrevised = ['Bullet Revised', .72, .079, 616, 251, 15E14, 4.71E14, 1.5E14, .47E14]
a1240 = ['A1240', .987, .099, 394, 118, 4.19E14, .99E14, 4.58E14, 1.4E14]
a3411 = ['A3411', 1.4, .2, 80, 170, 14E14, 5e14, 18e14, 5e14]
macsj1149 = ['MACSJ1149', .995, .064, 302, 219, 16.7E14, 1.3E14, 10.9E14, 3.4E14]
macsj1149revised = ['MACSJ1149', .995, .128, 302, 438, 16.7E14, 2.6E14, 10.9E14, 6.8E14]
macsj1752 = ['MACSJ1752', 1.145, .115, 114, 158, 12.04E14, 2.59E14, 13.22E14, 3.14E14]
zwci0008 = ['ZWCI0008', .924, .243, 92, 164, 5.7E14, 2.8E14, 1.2E14, 1.4E14]
zwci1856 = ['ZWCI1856', .925, .093, 189, 267, 9.66E14, 4.06E14, 7.6E14, 4.05E14]
a3667 = ['A3667', 1, .1, 525, 108, 14.59E14, 2.74E14, 13.26E14, 2.67E14]
a3667revised = ['A3667', 1, .2, 525, 206, 14.59E14, 5.48E14, 13.26E14, 5.34E14]
elgordo = ['El Gordo', .7, .1, 476, 242, 13.8E14, 2.2E14, 1.8E14, 2E14]
a3376 = ['A3376', 1.096, .066, 181, 147, 3.0E14, 1.7E14, 0.9E14, 0.8E14]
macsj0025 = ['MACSJ0025', .518, .116, 100, 80, 2.5E14, 1.7E14, 2.6E14, 1.4E14]

A1 = ['A1', 0.5, .2, 0, 150, 1E14, 1E14, 1E14, 1E14]
A2 = ['A2', 1.0, .2, 0, 150, 1E14, 1E14, 1E14, 1E14]
A3 = ['A3', 1.5, .2, 0, 150, 1E14, 1E14, 1E14, 1E14]

B1 = ['B1', 0.5, .2, 500, 150, 1E14, 1E14, 1E14, 1E14]
B2 = ['B2', 1.0, .2, 500, 150, 1E14, 1E14, 1E14, 1E14]
B3 = ['B3', 1.5, .2, 500, 150, 1E14, 1E14, 1E14, 1E14]

C1 = ['C1', 0.5, .2, 1000, 150, 1E14, 1E14, 1E14, 1E14]
C2 = ['C2', 1.0, .2, 1000, 150, 1E14, 1E14, 1E14, 1E14]
C3 = ['C3', 1.5, .2, 1000, 150, 1E14, 1E14, 1E14, 1E14]


#Pairs
listofpairs = []
generallist = [A1,B1,C1,A2,B2,C2,A3,B3,C3]
clusterlist = [musketball, ciza, rxcj1314, bullet, bulletrevised, a1240, a3411, macsj1149, macsj1149revised, macsj1752, zwci0008, zwci1856, a3667, a3667revised, elgordo, a3376, macsj0025]


if generalmass == True:
	fm = open("GeneralMassPDFsxxx.txt", "w")
	for a in generallist: listofpairs.append(a)
if generalpericenter == True:
	fp = open("GeneralPericenterPDFsxxx.txt", "w")
	if generalmass == False:
		for a in generallist: listofpairs.append(a)
if individualclusters == True:
	fc = open("ClusterPDFsxxx.txt", "w")
	for a in clusterlist: listofpairs.append(a)
#assign input values for each cluster

for cluster in listofpairs:
	print cluster
	sepmean   = cluster[1]
	sepsig  = cluster[2]

	velmean   = cluster[3]
	velsig  = cluster[4]

	massamean = cluster[5]
	massasig  = cluster[6]

	massbmean = cluster[7]
	massbsig  = cluster[8]

	anglehist    = [0] * 51
	anglehistsep100 = [0] * 51
	anglehistsep300 = [0] * 51
	anglehistsep500 = [0] * 51
	anglehistsep700 = [0] * 51
	anglehistmass5 = [0] * 51
	anglehistmass10 = [0] * 51
	anglehistmass15 = [0] * 51
	anglehistmasshigh = [0] * 51


	r = 0
	h = 0
	#cycle through the simulation catalog
	for i in range(len(pairid)):
		if i%100 == 0:
			print float(i)/float(len(pairid))

		#calculate mass probabilities
		#this is done by fitting both halos to each cluster in the merger, then adding the probabilities of a-a + b-b, and a-b + b-a

		mass_a_a_prob = (math.exp(((massamean-massa[i])*(massa[i]-massamean))/(2*massasig*massasig)))

		mass_a_b_prob = (math.exp(((massamean-massb[i])*(massb[i]-massamean))/(2*massasig*massasig)))

		mass_b_a_prob = (math.exp(((massbmean-massa[i])*(massa[i]-massbmean))/(2*massbsig*massbsig)))

		mass_b_b_prob = (math.exp(((massbmean-massb[i])*(massb[i]-massbmean))/(2*massbsig*massbsig)))

		totalmass = massa[i] + massb[i]
		pass_rel_vel_angle = math.atan(abs(passvel_y[i]/passvel_z[i]))

		#calculate rough estimate of the pericenter distance of this sim pair
		sepnumber = lowsep[i]*math.sin(pass_rel_vel_angle)
		pericenterhistogram.append(sepnumber)


		area_counter = 0
		total_divisor_points = 0

		theta = -.0314159265
		total_divisor_points = 0


		a = 0
		b = -1
		phi = 0
		#start "observing" from different points on the sphere

		while(theta < 3.14):
			b += 1
			theta = theta + (3.14159265/100)
			divisor = 100 * abs(math.sin(theta))
			total_divisor_points += divisor

			points = int(divisor)
			if points == 0:
				points = 1
			r = 0
			phi = 0
			while(phi < 6.28):
				a += 1
				phi = phi + 3.14159265/float(points)
				v_y = vel_y[i]
				v_z = vel_z[i]

				p = separation[i]

				#find the observed velocities and separation at this viewing angle
				obsvel = abs(math.sin(phi)*math.sin(theta)*v_y+math.cos(theta)*v_z)
				if(obsvel < 0.0):
					obsvel = -obsvel
				obssep = abs(p*math.sin(theta))

				#calculate the probabilities of each velocity and separation
				vel_prob = (math.exp(((velmean-obsvel)*(obsvel-velmean))/(2*velsig*velsig)))

				sep_prob = (math.exp(((sepmean-obssep)*(obssep-sepmean))/(2*sepsig*sepsig)))

				total_prob_mass = vel_prob*sep_prob*(mass_a_a_prob*mass_b_b_prob+mass_a_b_prob*mass_b_a_prob)
				total_prob = vel_prob*sep_prob



				if generalmass == True and sepnumber < .3 and cluster in generallist:
					if b < 50:
						h = b
						anglehist[h] += total_prob
						if totalmass < 5E14:
							anglehistmass5[h] += total_prob
						elif totalmass < 10E14:
							anglehistmass10[h] += total_prob
						elif totalmass < 15E14:
							anglehistmass15[h] += total_prob
						else:
							anglehistmasshigh[h] += total_prob
					elif b == 50:
						h = b
						anglehist[h] += 2*total_prob
						if totalmass < 5E14:
							anglehistmass5[h] += 2*total_prob
						elif totalmass < 10E14:
							anglehistmass10[h] += 2*total_prob
						elif totalmass < 15E14:
							anglehistmass15[h] += 2*total_prob
						else:
							anglehistmasshigh[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						anglehist[h] += total_prob
						if totalmass < 5E14:
							anglehistmass5[h] += total_prob
						elif totalmass < 10E14:
							anglehistmass10[h] += total_prob
						elif totalmass < 15E14:
							anglehistmass15[h] += total_prob
						else:
							anglehistmasshigh[h] += total_prob

				if generalpericenter == True and cluster in generallist:
					if b < 50:
						h = b
						anglehist[h] += total_prob
						if sepnumber < .1:
							anglehistsep100[h] += total_prob
						elif sepnumber < .3:
							anglehistsep300[h] += total_prob
						elif sepnumber < .5:
							anglehistsep500[h] += total_prob
						else:
							anglehistsep700[h] += total_prob
					elif b == 50:
						h = b
						anglehist[h] += 2*total_prob
						if sepnumber < .1:
							anglehistsep100[h] += 2*total_prob
						elif sepnumber < .3:
							anglehistsep300[h] += 2*total_prob
						elif sepnumber < .5:
							anglehistsep500[h] += 2*total_prob
						else:
							anglehistsep700[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						anglehist[h] += total_prob
						if sepnumber < .1:
							anglehistsep100[h] += total_prob
						elif sepnumber < .3:
							anglehistsep300[h] += total_prob
						elif sepnumber < .5:
							anglehistsep500[h] += total_prob
						else:
							anglehistsep700[h] += total_prob



				if individualclusters == True and sepnumber < .3 and cluster in clusterlist:
					if b < 50:
						h = b
						anglehist[h] += total_prob
					elif b == 50:
						h = b
						anglehist[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						anglehist[h] += total_prob

	if generalmass == True and cluster in generallist:
		fm.write( cluster[0] + '= [' + str(anglehistmass5) + ', ' + str(anglehistmass10) + ', ' + str(anglehistmass15) + ', ' + str(anglehistmasshigh) +']\n')
	if generalpericenter == True and cluster in generallist:
		fp.write( cluster[0] + '= [' + str(anglehistsep100) + ', ' + str(anglehistsep300) + ', ' + str(anglehistsep500) + ', ' + str(anglehistsep700) +']\n')
	if individualclusters == True and cluster in clusterlist:
		fc.write( cluster[0] + '= [' + str(anglehist) + ']\n')

	plt.hist(pericenterhistogram)
plt.show()


#have everything write to the correct files and you're golden pony boy
