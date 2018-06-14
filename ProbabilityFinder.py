import numpy as np
import math
import matplotlib.pyplot as plt





#This lists all the inputs for each system
#Name, Separation, Separation Sigma, LOS Vel, LOS Vel Sigma, MassA, MassA Sigma, MassB, MassB Sigma]
musketball = ['Musketball', 1.0, .14, 670, 330, 3.1E14, 1.2E14, 1.7E14, 2.0E14, '31']
ciza = ['Ciza', 1.3, .13, 69, 190, 11E14, 3.7E14, 9.8E14, 3.8E14, '60']
rxcj1314 = ['RXCJ1314', .54, .23, 1523, 149, 6.07E14, 1.8E14, 7.17E14, 2.8E14, '52']
bullet = ['Bullet', .72, .025, 616, 80, 15E14, 1.5E14, 1.5E14, .15E14, '48']
bulletrevised = ['Bulletrevised', .72, .075, 616, 80, 15E14, 1.5E14, 1.5E14, .15E14, '48']
a1240 = ['A1240', .987, .099, 394, 118, 4.19E14, .99E14, 4.58E14, 1.4E14, '59']
a3411 = ['A3411', 1.4, .2, 80, 170, 14E14, 5e14, 18e14, 5e14, '63']
macsj1149 = ['MACSJ1149', .995, .064, 302, 219, 16.7E14, 1.3E14, 10.9E14, 3.4E14, '30']
macsj1752 = ['MACSJ1752', 1.145, .115, 114, 158, 12.04E14, 2.59E14, 13.22E14, 3.14E14, '44']
zwci0008 = ['ZWCI0008', .924, .243, 92, 164, 5.7E14, 2.8E14, 1.2E14, 1.4E14, '75']
zwci1856 = ['ZWCI1856', .925, .093, 189, 267, 9.66E14, 4.06E14, 7.6E14, 4.05E14, '48']
a3667 = ['A3667', 1, .1, 525, 108, 14.59E14, 2.74E14, 13.26E14, 2.67E14, '77']
#elgordo attributes were changed to answer questions from readers and are no longer accurate
#elgordo = ['ElGordo', .7, .1, 1820, 242, 13.8E14, 2.2E14, 7.8E14, 2E14, '12']
#elgordorevised = ['ElGordorevised', .7, .1, 1820, 242, 25E14, 2.2E14, 3.6E14, 2E14, '77']
a3376 = ['A3376', 1.096, .066, 181, 147, 3.0E14, 1.7E14, 0.9E14, 0.8E14, '77']
macsj0025 = ['MACSJ0025', .518, .116, 100, 80, 2.5E14, 1.7E14, 2.6E14, 1.4E14, '27']
#macsj0416 = ['MACSJ0416', , , , , , , , , '42']

#General inputs for representative, fake clusters
A1 = ['A1', 0.5, .2, 0, 150, 1E14, 1E14, 1E14, 1E14]
A2 = ['A2', 1.0, .2, 0, 150, 1E14, 1E14, 1E14, 1E14]
A3 = ['A3', 1.5, .2, 0, 150, 1E14, 1E14, 1E14, 1E14]

B1 = ['B1', 0.5, .2, 500, 150, 1E14, 1E14, 1E14, 1E14]
B2 = ['B2', 1.0, .2, 500, 150, 1E14, 1E14, 1E14, 1E14]
B3 = ['B3', 1.5, .2, 500, 150, 1E14, 1E14, 1E14, 1E14]

C1 = ['C1', 0.5, .2, 1000, 150, 1E14, 1E14, 1E14, 1E14]
C2 = ['C2', 1.0, .2, 1000, 150, 1E14, 1E14, 1E14, 1E14]
C3 = ['C3', 1.5, .2, 1000, 150, 1E14, 1E14, 1E14, 1E14]


#write cluster variable names in list of pairs
listofpairs = []

#this isn't really important
probabilityhistogram = []

#does the calculation separately for each cluster pair
for cluster in listofpairs:

	#open the savefile to write to
	f = open('DataFiles/ClusterPDF_' + cluster[0] + '.txt', 'w')

	#unpack the data at the correct snapshot
	massa, massb, separation, vel_z, vel_y, pericenter = np.loadtxt('final_data/final_data_' + cluster[9] + '.txt', delimiter = ',', unpack = True)

	print cluster[0] #cluster name

	#assign the variables to the correct values for the cluster
	sepmean   = cluster[1]
	sepsig  = cluster[2]

	velmean   = cluster[3]
	velsig  = cluster[4]

	massamean = cluster[5]
	massasig  = cluster[6]

	massbmean = cluster[7]
	massbsig  = cluster[8]
	clusterredshift = cluster[9]


	#these are the lists all the data is saved in
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
	for i in range(len(massa)):
		totalprobabilityofanalog = 0

		#keep track of percentage done
		if i%100 == 0:
			print float(i)/float(len(massa))

		#calculate mass probabilities
		#this is done by fitting both halos to each cluster in the merger, then adding the probabilities of a-a + b-b, and a-b + b-a
		mass_a_a_prob = (math.exp(((massamean-massa[i])*(massa[i]-massamean))/(2*massasig*massasig)))

		mass_a_b_prob = (math.exp(((massamean-massb[i])*(massb[i]-massamean))/(2*massasig*massasig)))

		mass_b_a_prob = (math.exp(((massbmean-massa[i])*(massa[i]-massbmean))/(2*massbsig*massbsig)))

		mass_b_b_prob = (math.exp(((massbmean-massb[i])*(massb[i]-massbmean))/(2*massbsig*massbsig)))

		#calculate total mass (only relavent for the general clusters)
		totalmass = (massa[i] + massb[i])/1E15

		#save the pericenter distance
		sepnumber = pericenter[i]

		#counters for the probability calculation
		area_counter = 0
		total_divisor_points = 0
		theta = -.0314159265
		a = 0
		b = -1
		phi = 0

		#start "observing" from different points on the sphere
		while(theta < 3.14): # do a half circle in theta
			b += 1
			theta = theta + (3.14159265/100)
			divisor = 100 * abs(math.sin(theta))
			total_divisor_points += divisor

			points = int(divisor)
			if points == 0:
				points = 1
			r = 0
			phi = 0
			while(phi < 6.28): #do a full circle in phi
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


				#for the generalized cluster, you have to save the data to all the histograms differently,
				#but I guess I deleted that part a while ago and I don't want to rewrite it without need



				#if the cluster has a small enough pericenter, we add the probability to the correct index
				#in the histogram
				if sepnumber < .3:
					totalprobabilityofanalog += total_prob_mass
					if b < 50:
						h = b
						anglehist[h] += total_prob
					elif b == 50:
						h = b
						anglehist[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						anglehist[h] += total_prob

		probabilityhistogram.append(totalprobabilityofanalog)



	#write it out to the save file
	f.write( cluster[0] + '= ' + str(anglehist) + '\n')
print probabilityhistogram
