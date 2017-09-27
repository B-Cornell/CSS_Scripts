import numpy as np
import math
import matplotlib.pyplot as plt


pairid, rockstara, rockstarb, massa, massb, radiusa, radiusb, separation, vel_z, vel_y = np.loadtxt('trees/treefile.csv', delimiter = ',', unpack = True)

angles = [[0]]*25
for square in range(25):
	high = square
	while high > 4:
		high -=5
	low = square/5

	#sepmean   = .5 + .2*low
	#sepsig  = .15 * sepmean

	velmean   = 300 * low
	velsig  = 150 + .1*velmean

	massmean = 1E14*(5*high)
	if massmean < 20:
		massmean = 2E14
	masssig  = .25*massmean
	if high == 0:
		massratiolow = 1
		massratiohigh = 1.5
	elif high == 1:
		massratiolow = 1.5
		massratiohigh = 2.5
	elif high == 2: 
		massratiolow = 2.5
		massratiohigh = 5
	elif high == 3:
		massratiolow = 5
		massratiohigh = 8
	else:
		massratiolow = 8
		massratiohigh = 1000
	
	print massratiolow
	print velmean
	print '\n'

	anglehist = [0] * 51
	r = 0
	h = 0

	for i in range(len(pairid)):
		massratio = massa[i]/massb[i]
		if massratio < 1:
			massratio = 1/massratio
		area_counter = 0
		total_divisor_points = 0

		theta = -.0314159265
		total_divisor_points = 0

		#rel_vel_angle = math.atan(abs(vel_y[i]/vel_z[i])) * (180.0 / 3.14159265)
		
		b = -1
		phi = 0
		if massratio < massratiohigh and massratio > massratiolow and separation[i] > .1:
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
				
					phi = phi + 3.14159265/float(points)
					v_y = vel_y[i]
					v_z = vel_z[i]

					p = separation[i]

					obsvel = abs(math.sin(phi)*math.sin(theta)*v_y+math.cos(theta)*v_z)
					if(obsvel < 0.0):
						obsvel = -obsvel
					obssep = abs(p*math.sin(theta))

					vel_prob = (math.exp(((velmean-obsvel)*(obsvel-velmean))/(2*velsig*velsig)))

					#sep_prob = (math.exp(((sepmean-obssep)*(obssep-sepmean))/(2*sepsig*sepsig)))

					#mass_prob = (math.exp(((massmean-mass)*(mass-massmean))/(2*masssig*masssig)))

					total_prob = vel_prob#*mass_prob
					area_counter += total_prob
					if b < 50:
						h = b
						anglehist[b] += total_prob
					elif b == 50:
						h = b
						anglehist[b] += 2*total_prob
					else:
						h = 50 - (b-50)
						anglehist[h] += total_prob
		
			calculatedprob = area_counter
	
	
	angles[square] = anglehist 


fig, axes = plt.subplots(nrows = 5, ncols = 5)
fig.subplots_adjust(hspace = 0, wspace = 0)
ninety = [6.93889390391e-18, 0.0314159265, 0.062831853, 0.0942477795, 0.125663706, 0.1570796325, 0.188495559, 0.2199114855, 0.251327412, 0.2827433385, 0.314159265, 0.3455751915, 0.376991118, 0.4084070445, 0.439822971, 0.4712388975, 0.502654824, 0.5340707505, 0.565486677, 0.5969026035, 0.62831853, 0.6597344565, 0.691150383, 0.7225663095, 0.753982236, 0.7853981625, 0.816814089, 0.8482300155, 0.879645942, 0.9110618685, 0.942477795, 0.9738937215, 1.005309648, 1.0367255745, 1.068141501, 1.0995574275, 1.130973354, 1.1623892805, 1.193805207, 1.2252211335, 1.25663706, 1.2880529865, 1.319468913, 1.3508848395, 1.382300766, 1.4137166925, 1.445132619, 1.4765485455, 1.507964472, 1.5393803985, 1.570796325]

for c in range(5):
	for r in range(5):
		axes[r,c].set_yticks([])
		axes[r,c].set_xticks([])
		axes[r,c].plot(ninety, angles[c*5+4-r] ) 
		if r == 4 and c == 2:
			axes[r,c].set_xlabel('LOS Velocity (km/s)\n0, 300, 600, 900, 1200')
		if r == 2 and c == 0:
			axes[r,c].set_ylabel('Mass Ratio \n1:1-1.5, 1:1.5-2.5, 1:2.5-5, 1:5-8, 1:8+')
			#axes[r,c].set_ylabel('LOS Velocity (km/s)\n0, 300, 600, 900, 1200') 
plt.show()
		    
#There are 12632 visualization points.      
