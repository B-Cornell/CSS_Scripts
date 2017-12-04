import numpy as np
import math

pairid, rockstara, rockstarb, massa, massb, radiusa, radiusb, separation, vel_z, vel_y, passsnap, lowsep = np.loadtxt('trees/treefile.csv', delimiter = ',', unpack = True)


#This lists all the inputs for each system
#Name, Separation, Separation Sigma, LOS Vel, LOS Vel Sigma, MassA, MassA Sigma, MassB, MassB Sigma]
musketball = ['Musketball', 1.0, .14, 670, 330, 3.1E14, 1.2E14, 1.7E14, 2.0E14]
ciza = ['Ciza', 1.3, .13, 69, 190, 11E14, 3.7E14, 9.8E14, 3.8E14]
rxcj1314 = ['RXCJ1314', .54, .23, 1523, 149, 6.07E14, 1.8E14, 7.17E14, 2.8E14]
bullet = ['Bullet', .72, .025, 616, 80, 15E14, 1.5E14, 1.5E14, .15E14]
a1240 = ['A1240', .987, .099, 394, 118, 4.19E14, .99E14, 4.58E14, 1.4E14]
a3411 = ['A3411', 1.4, .2, 80, 170, 14E14, 5e14, 18e14, 5e14]
macsj1149 = ['MACSJ1149', .995, .064, 302, 219, 16.7E14, 1.3E14, 10.9E14, 3.4E14]
macsj1752 = ['MACSJ1752', 1.145, .115, 114, 158, 12.04E14, 2.59E14, 13.22E14, 3.14E14]
zwci0008 = ['ZWCI0008', .924, .243, 92, 164, 5.7E14, 2.8E14, 1.2E14, 1.4E14]
zwci1856 = ['ZWCI1856', .925, .093, 189, 267, 9.66E14, 4.06E14, 7.6E14, 4.05E14]
a3667 = ['A3667', 1, .1, 525, 108, 14.59E14, 2.74E14, 13.26E14, 2.67E14]
elgordo = ['El Gordo', .7, .1, 586, 96, 13.8E14, 2.2E14, 1.8E14, 2E14]

listofpairs = [musketball, ciza, rxcj1314, bullet, a1240, a3411, macsj1149, macsj1752, zwci0008, zwci1856, a3667, elgordo]
f = open("anglehistsbysmallsep.txt", "w")


#assign input values for each cluster
for cluster in listofpairs:
	sepmean   = cluster[1]
	sepsig  = cluster[2]

	velmean   = cluster[3]
	velsig  = cluster[4]

	massamean = cluster[5]
	massasig  = cluster[6]

	massbmean = cluster[7]
	massbsig  = cluster[8]

	anglehist100 = [0] * 51
	anglehist200 = [0] * 51
	anglehist350 = [0] * 51
	anglehist700 = [0] * 51


	r = 0
	h = 0
	#cycle through the simulation catalog
	for i in range(len(pairid)):
		#calculate mass probabilities
		#this is done by fitting both halos to each cluster in the merger, then adding the probabilities of a-a + b-b, and a-b + b-a
		mass_a_a_prob = (math.exp(((massamean-massa[i])*(massa[i]-massamean))/(2*massasig*massasig)))

		mass_a_b_prob = (math.exp(((massamean-massb[i])*(massb[i]-massamean))/(2*massasig*massasig)))

		mass_b_a_prob = (math.exp(((massbmean-massa[i])*(massa[i]-massbmean))/(2*massbsig*massbsig)))

		mass_b_b_prob = (math.exp(((massbmean-massb[i])*(massb[i]-massbmean))/(2*massbsig*massbsig)))
	
	
		rel_vel_angle = math.atan(abs(vel_y[i]/vel_z[i])) * (180.0 / 3.14159265)
		#calculate rough estimate of the impact parameter of this sim pair
		sepnumber = lowsep[i]*math.sin(rel_vel_angle)

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

				


				total_prob = vel_prob*sep_prob*(mass_a_a_prob*mass_b_b_prob+mass_a_b_prob*mass_b_a_prob)
				if sepnumber < .1:
					if b < 50:
						h = b
						anglehist100[h] += total_prob
						anglehist200[h] += total_prob
						anglehist350[h] += total_prob
						anglehist700[h] += total_prob
					elif b == 50:
						h = b
						anglehist100[h] += 2*total_prob
						anglehist200[h] += 2*total_prob
						anglehist350[h] += 2*total_prob
						anglehist700[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						anglehist100[h] += total_prob
						anglehist200[h] += total_prob
						anglehist350[h] += total_prob
						anglehist700[h] += total_prob
				elif sepnumber < .2:
					if b < 50:
						h = b
						anglehist200[h] += total_prob
						anglehist350[h] += total_prob
						anglehist700[h] += total_prob
					elif b == 50:
						h = b
						anglehist200[h] += 2*total_prob
						anglehist350[h] += 2*total_prob
						anglehist700[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						anglehist200[h] += total_prob
						anglehist350[h] += total_prob
						anglehist700[h] += total_prob
				elif sepnumber < .35:
					if b < 50:
						h = b
						anglehist350[h] += total_prob
						anglehist700[h] += total_prob
					elif b == 50:
						h = b
						anglehist350[h] += 2*total_prob
						anglehist700[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						anglehist350[h] += total_prob
						anglehist700[h] += total_prob
				else:
					if b < 50:
						h = b
						anglehist700[h] += total_prob
					elif b == 50:
						h = b
						anglehist700[h] += 2*total_prob
					else:
						h = 50 - (b-50)
						anglehist700[h] += total_prob
	f.write( cluster[0] + '\n' + str(anglehist100) + '\n' + str(anglehist200) + '\n' + str(anglehist350) + '\n' + str(anglehist700) + '\n')
	print  cluster[0] + '\n' + str(anglehist100) + '\n' + str(anglehist200) + '\n' + str(anglehist350) + '\n' + str(anglehist700)
   
#There are 12632 visualization points.      
