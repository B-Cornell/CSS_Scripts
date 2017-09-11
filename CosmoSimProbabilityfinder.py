import numpy as np
import math

pairid, rockstara, rockstarb, massa, massb, radiusa, radiusb, separation, vel_z, vel_y = np.loadtxt('treefile.csv', delimiter = ',', unpack = True)

massamean = 11.0E14 
massbmean = 9.8E14
massasig  = 3.45E14
massbsig  = 3.15E14
sepmean   = 1.1
velmean   = 69
sepsig  = .2
velsig  = 340

anglehist = [0] * 104
f = open('CIZA.csv', 'w')

for i in range(len(pairid)):
	area_counter = 0
	total_divisor_points = 0

	theta = -.0314159265
	total_divisor_points = 0

	rel_vel_angle = math.atan(abs(vel_y[i]/vel_z[i])) * (180.0 / 3.14159265)
	b = -1
	phi = 0
	while(theta <= 3.14159265):
		b += 1
		theta = theta + (3.14159265/100)
		divisor = 100 * abs(math.sin(theta))
		total_divisor_points += divisor

		points = int(divisor)
		if points != 0:
			phi = -3.14159265/float(points)

		while(phi < 6.2831853 and points>0):
			phi = phi + 3.14159265/float(points)

			v_y = vel_y[i]
			v_z = vel_z[i]

			p = separation[i]

			obsvel = abs(math.sin(phi)*math.sin(theta)*v_y+math.cos(theta)*v_z)
			if(obsvel < 0.0):
				obsvel = -obsvel
			obssep = abs(p*math.sin(theta))
			if(obssep < 0):
				obssep = -obssep


			vel_prob = (math.exp(((velmean-obsvel)*(obsvel-velmean))/(2*velsig*velsig)))

			sep_prob = (math.exp(((sepmean-obssep)*(obssep-sepmean))/(2*sepsig*sepsig)))

			#mass_a_a_prob = (math.exp(((massamean-massa[i])*(massa[i]-massamean))/(2*massasig*massasig)))

			#mass_a_b_prob = (math.exp(((massamean-massb[i])*(massb[i]-massamean))/(2*massasig*massasig)))

			#mass_b_a_prob = (math.exp(((massbmean-massa[i])*(massa[i]-massbmean))/(2*massbsig*massbsig)))

			#mass_b_b_prob = (math.exp(((massbmean-massb[i])*(massb[i]-massbmean))/(2*massbsig*massbsig)))


			total_prob = vel_prob*sep_prob#*(mass_a_a_prob*mass_b_b_prob+mass_a_b_prob*mass_b_a_prob)
			area_counter += total_prob
			anglehist[b] += total_prob
	calculatedprob = area_counter
	f.write( str(massa[i]) + ', ' + str(massb[i]) + ', ' + str(p) + ', ' + str(v_z) + ', ' + str(v_y) + ', ' + str(rel_vel_angle) + ', ' + str(calculatedprob) + '\n')
			    
	print str(massa[i]) + ', ' + str(massb[i]) + ', ' + str(p) + ', ' + str(v_z) + ', ' + str(v_y) + ', ' + str(rel_vel_angle) + ', ' + str(calculatedprob) + '\n'
print anglehist             
                
