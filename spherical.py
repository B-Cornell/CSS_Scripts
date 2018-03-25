import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pairid, rockstara, rockstarb, massa, massb, radiusa, radiusb, separation, vel_z, vel_y, passsnap, lowsep, passvel_z, passvel_y = np.loadtxt('trees/treefilepostmerger.csv', delimiter = ',', unpack = True)


#This lists all the inputs for each system
#Name, Separation, Separation Sigma, LOS Vel, LOS Vel Sigma, MassA, MassA Sigma, MassB, MassB Sigma]

general = ['general', .65, .2, 1000, 100]
 
listofpairs =[general] 


#assign input values for each cluster
for cluster in listofpairs:
	sepmean   = cluster[1]
	sepsig  = cluster[2]

	velmean   = cluster[3]
	velsig  = cluster[4]


	xs = []
	ys = []
	zs = []
	prob = []

	anglehist100 = [0] * 51
	anglehist200 = [0] * 51
	anglehist350 = [0] * 51
	anglehist700 = [0] * 51
	r = 0
	h = 0
	#cycle through the simulation catalog
	for i in range(20):
		
		rel_vel_angle = math.atan(abs(passvel_y[i]/passvel_z[i]))
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
		if sepnumber <= .3:
			while(theta < 3.14):
				b += 1
				theta = theta + (3.14159265/70)
				divisor = 70 * abs(math.sin(theta))
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

				


					total_prob = vel_prob*sep_prob
					zs.append(math.cos(theta))
					ys.append(math.sin(theta)*math.sin(phi))
					xs.append(math.sin(theta)*math.cos(phi))
					prob.append(total_prob)
		
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.scatter(xs, ys, zs, c = prob, cmap = 'binary', edgecolors = 'w')


		plt.show()

