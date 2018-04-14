import numpy as np
import math
import matplotlib.pyplot as plt
import sys

generalmass, generalpericenter, individualclusters, binned, notbinned, three, random = False, False, False, False, False, False, False
for a in sys.argv:
	if a == 'mass':
		generalmass = True
	if a == 'pericenter':
		generalpericenter = True
	if a == 'clusters':
		individualclusters = True
	if a == 'bins':
		binned = True
	if a == 'cuts':
		notbinned = True
	if a == 'three':
		three = True
	if a == 'random':
		random = True




pairid, rockstara, rockstarb, massa, massb, radiusa, radiusb, separation, vel_z, vel_y, passsnap, lowsep, passvel_z, passvel_y = np.loadtxt('trees/treefilepostmerger.csv', delimiter = ',', unpack = True)


#This lists all the inputs for each system
#Name, Separation, Separation Sigma, LOS Vel, LOS Vel Sigma, MassA, MassA Sigma, MassB, MassB Sigma]
musketball = ['Musketball', 1.0, .14, 670, 330, 3.1E14, 1.2E14, 1.7E14, 2.0E14]
ciza = ['Ciza', 1.3, .13, 69, 190, 11E14, 3.7E14, 9.8E14, 3.8E14]
rxcj1314 = ['RXCJ1314', .54, .23, 1523, 149, 6.07E14, 1.8E14, 7.17E14, 2.8E14]
bullet = ['Bullet', .72, .025, 616, 80, 15E14, 1.5E14, 1.5E14, .15E14]
bulletrevised = ['BulletRevised', .72, .079, 616, 251, 15E14, 4.71E14, 1.5E14, .47E14]
a1240 = ['A1240', .987, .099, 394, 118, 4.19E14, .99E14, 4.58E14, 1.4E14]
a3411 = ['A3411', 1.4, .2, 80, 170, 14E14, 5e14, 18e14, 5e14]
macsj1149 = ['MACSJ1149', .995, .064, 302, 219, 16.7E14, 1.3E14, 10.9E14, 3.4E14]
macsj1752 = ['MACSJ1752', 1.145, .115, 114, 158, 12.04E14, 2.59E14, 13.22E14, 3.14E14]
zwci0008 = ['ZWCI0008', .924, .243, 92, 164, 5.7E14, 2.8E14, 1.2E14, 1.4E14]
zwci1856 = ['ZWCI1856', .925, .093, 189, 267, 9.66E14, 4.06E14, 7.6E14, 4.05E14]
a3667 = ['A3667', 1, .1, 525, 108, 14.59E14, 2.74E14, 13.26E14, 2.67E14]
elgordo = ['ElGordo', .7, .1, 476, 242, 13.8E14, 2.2E14, 1.8E14, 2E14]
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

#f = open('ThreePDFsxxx.txt', "w")
generallist = [A1,B1,C1,A2,B2,C2,A3,B3,C3]
clusterlist = [musketball, ciza, rxcj1314, bullet, a1240, a3411, macsj1149, macsj1752, zwci0008, zwci1856, a3667, elgordo, a3376, macsj0025]
revisedlist = [bulletrevised, a3667, macsj1149]
randomlist = [macsj0025,macsj1149]

if notbinned == True:
	if generalmass == True:
		fmn = open("DataFiles/GeneralMassPDFs_cuts_peri300.txt", "w")
		for a in generallist: listofpairs.append(a)
	if generalpericenter == True:
		fpn = open("DataFiles/GeneralPericenterPDFs_cuts.txt", "w")
		if generalmass == False:
			for a in generallist: listofpairs.append(a)
if binned == True:
	if generalmass == True:
		fmb = open("DataFiles/GeneralMassPDFs_bins_peri300.txt", "w")
		for a in generallist: listofpairs.append(a)
	if generalpericenter == True:
		fpb = open("DataFiles/GeneralPericenterPDFs_bins.txt", "w")
		if generalmass == False:
			for a in generallist: listofpairs.append(a)
if individualclusters == True:
	fc = open("DataFiles/ClusterPDFs.txt", "w")
	for a in clusterlist: listofpairs.append(a)
if three == True:
	ft = open("DataFiles/RevisedPDFs.txt", "w")
	if individualclusters == True:
		listofpairs.append(bulletrevised)
	else:
		for a in revisedlist: listofpairs.append(a)
if random == True:
	fr = open("DataFiles/ExtraPDFs.txt", "w")
	for a in randomlist: listofpairs.append(a)
#assign input values for each cluster

for cluster in listofpairs:
	print cluster[0]
	sepmean   = cluster[1]
	sepsig  = cluster[2]

	velmean   = cluster[3]
	velsig  = cluster[4]

	massamean = cluster[5]
	massasig  = cluster[6]

	massbmean = cluster[7]
	massbsig  = cluster[8]

	anglehist    = [0] * 51
	anglehistrandom = [0] * 51

	anglehistsep100b = [0] * 51
	anglehistsep300b = [0] * 51
	anglehistsep500b = [0] * 51
	anglehistsep700b = [0] * 51
	anglehistmass5b = [0] * 51
	anglehistmass10b = [0] * 51
	anglehistmass15b = [0] * 51
	anglehistmasshighb = [0] * 51

	anglehistsep100n = [0] * 51
	anglehistsep300n = [0] * 51
	anglehistsep500n = [0] * 51
	anglehistsep700n = [0] * 51
	anglehistmass5n = [0] * 51
	anglehistmass10n = [0] * 51
	anglehistmass15n = [0] * 51
	anglehistmasshighn = [0] * 51


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

		totalmass = (massa[i] + massb[i])/1E15

		pass_rel_vel_angle = math.atan(abs(passvel_y[i]/passvel_z[i]))

		#calculate rough estimate of the pericenter distance of this sim pair
		sepnumber = lowsep[i]*math.sin(pass_rel_vel_angle)


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



				if generalmass == True and sepnumber < .3 and notbinned == True and cluster in generallist:
					if b < 50:
						h = b
						if totalmass < 5E14:
							anglehistmass5n[h] += total_prob
						if totalmass < 10E14:
							anglehistmass10n[h] += total_prob
						if totalmass < 15E14:
							anglehistmass15n[h] += total_prob
						if totalmass > 0:
							anglehistmasshighn[h] += total_prob
					elif b == 50:
						h = b
						if totalmass < 5E14:
							anglehistmass5n[h] += 2*total_prob
						if totalmass < 10E14:
							anglehistmass10n[h] += 2*total_prob
						if totalmass < 15E14:
							anglehistmass15n[h] += 2*total_prob
						if totalmass > 0:
							anglehistmasshighn[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						if totalmass < 5E14:
							anglehistmass5n[h] += total_prob_mass
						if totalmass < 10E14:
							anglehistmass10n[h] += total_prob_mass
						if totalmass < 15E14:
							anglehistmass15n[h] += total_prob_mass
						if totalmass > 0:
							anglehistmasshighn[h] += total_prob_mass

				if generalpericenter == True and notbinned == True and cluster in generallist:
					if b < 50:
						h = b

						if sepnumber < .1:
							anglehistsep100n[h] += total_prob
						if sepnumber < .3:
							anglehistsep300n[h] += total_prob
						if sepnumber < .5:
							anglehistsep500n[h] += total_prob
						if sepnumber < .7:
							anglehistsep700n[h] += total_prob
					elif b == 50:
						h = b
						if sepnumber < .1:
							anglehistsep100n[h] += 2*total_prob
						if sepnumber < .3:
							anglehistsep300n[h] += 2*total_prob
						if sepnumber < .5:
							anglehistsep500n[h] += 2*total_prob
						if sepnumber < .7:
							anglehistsep700n[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						if sepnumber < .1:
							anglehistsep100n[h] += total_prob
						if sepnumber < .3:
							anglehistsep300n[h] += total_prob
						if sepnumber < .5:
							anglehistsep500n[h] += total_prob
						if sepnumber < .7:
							anglehistsep700n[h] += total_prob

				if generalmass == True and sepnumber < .3 and binned == True and cluster in generallist:
					if b < 50:
						h = b
						if totalmass < 5E14:
							anglehistmass5b[h] += total_prob
						elif totalmass < 10E14:
							anglehistmass10b[h] += total_prob
						elif totalmass < 15E14:
							anglehistmass15b[h] += total_prob
						else:
							anglehistmasshighb[h] += total_prob
					elif b == 50:
						h = b
						if totalmass < 5E14:
							anglehistmass5b[h] += 2*total_prob
						elif totalmass < 10E14:
							anglehistmass10b[h] += 2*total_prob
						elif totalmass < 15E14:
							anglehistmass15b[h] += 2*total_prob
						else:
							anglehistmasshighb[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						if totalmass < 5E14:
							anglehistmass5b[h] += total_prob_mass
						elif totalmass < 10E14:
							anglehistmass10b[h] += total_prob_mass
						elif totalmass < 15E14:
							anglehistmass15b[h] += total_prob_mass
						else:
							anglehistmasshighb[h] += total_prob_mass

				if generalpericenter == True and binned == True and cluster in generallist:
					if b < 50:
						h = b
						if sepnumber < .1:
							anglehistsep100b[h] += total_prob
						elif sepnumber < .3:
							anglehistsep300b[h] += total_prob
						elif sepnumber < .5:
							anglehistsep500b[h] += total_prob
						else:
							anglehistsep700b[h] += total_prob
					elif b == 50:
						h = b
						if sepnumber < .1:
							anglehistsep100b[h] += 2*total_prob
						elif sepnumber < .3:
							anglehistsep300b[h] += 2*total_prob
						elif sepnumber < .5:
							anglehistsep500b[h] += 2*total_prob
						else:
							anglehistsep700b[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						if sepnumber < .1:
							anglehistsep100b[h] += total_prob
						elif sepnumber < .3:
							anglehistsep300b[h] += total_prob
						elif sepnumber < .5:
							anglehistsep500b[h] += total_prob
						else:
							anglehistsep700b[h] += total_prob

				if individualclusters == True and sepnumber < .3 and cluster in clusterlist:
					if b < 50:
						h = b
						anglehist[h] += total_prob_mass
					elif b == 50:
						h = b
						anglehist[h] += 2*total_prob_mass
					else:
						h = 50 - (b-50)
						anglehist[h] += total_prob_mass

				if three == True and sepnumber < .3 and cluster in revisedlist:
					if cluster == bulletrevised:
						if b < 50:
							h = b
							anglehist[h] += total_prob_mass
						elif b == 50:
							h = b
							anglehist[h] += 2*total_prob_mass
						else:
							h = 50 - (b-50)
							anglehist[h] += total_prob_mass
					else:
						if b < 50:
							h = b
							anglehist[h] += total_prob
						elif b == 50:
							h = b
							anglehist[h] += 2*total_prob
						else:
							h = 50 - (b-50)
							anglehist[h] += total_prob

				if random == True and sepnumber < .3 and cluster in randomlist:
					if b < 50:
						h = b
						anglehistrandom[h] += total_prob_mass
					elif b == 50:
						h = b
						anglehistrandom[h] += 2*total_prob_mass
					else:
						h = 50 - (b-50)
						anglehistrandom[h] += total_prob_mass



	if generalmass == True and cluster in generallist and binned == True:
		fmb.write( cluster[0] + '= [' + str(anglehistmass5b) + ', ' + str(anglehistmass10b) + ', ' + str(anglehistmass15b) + ', ' + str(anglehistmasshighb) +']\n')
	if generalpericenter == True and cluster in generallist:
		fpb.write( cluster[0] + '= [' + str(anglehistsep100b) + ', ' + str(anglehistsep300b) + ', ' + str(anglehistsep500b) + ', ' + str(anglehistsep700b) +']\n')

	if generalmass == True and cluster in generallist and notbinned == True:
		fmn.write( cluster[0] + '= [' + str(anglehistmass5n) + ', ' + str(anglehistmass10n) + ', ' + str(anglehistmass15n) + ', ' + str(anglehistmasshighn) +']\n')
	if generalpericenter == True and cluster in generallist:
		fpn.write( cluster[0] + '= [' + str(anglehistsep100n) + ', ' + str(anglehistsep300n) + ', ' + str(anglehistsep500n) + ', ' + str(anglehistsep700n) +']\n')

	if individualclusters == True and cluster in clusterlist:
		fc.write( cluster[0] + '= ' + str(anglehist) + '\n')
	if three == True and cluster in revisedlist:
		ft.write( cluster[0] + '= ' + str(anglehist) + '\n')
	if random == True and cluster in randomlist:
		fr.write( cluster[0] + ' = ' + str(anglehistrandom) + '\n')
