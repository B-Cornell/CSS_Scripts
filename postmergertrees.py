import numpy as np
import math
import sys

fulldata = True

for a in sys.argv:
	if a == 'old':

		fulldata = False


if fulldata == False:
	pairid, rockstara, rockstarb, massa, massb, radiusa, radiusb, separation, vel_z, vel_y, passsnap, lowsep, passvel_z, passvel_y = np.loadtxt('trees/treefile.csv', delimiter = ',', unpack = True)

	#f = open("trees/treefilepostmerger.csv", "w")
	goodpairs = 0
	for a in range(len(pairid)):
		if (separation[a] > lowsep[a]) or (separation[a] < lowsep[a] and vel_z[a] > 0):
			#f.write(str(pairid[a]) + ', ' + str(rockstara[a]) + ', ' + str(rockstarb[a]) + ', ' + str(massa[a]) + ', ' + str(massb[a]) + ', ' + str(radiusa[a]) + ', ' + str(radiusb[a]) + ', ' + str(separation[a]) + ', ' + str(vel_z[a]) + ', ' + str(vel_y[a]) + ', ' + str(passsnap[a]) + ', ' + str(lowsep[a]) + ', ' + str(passvel_z[a]) + ', ' + str(passvel_y[a]) + '\n')
			goodpairs += 1
	print goodpairs
	print len(pairid)
	#f.close()



else:

	totalogpairs = 0
	og_pairs = 0
	goodpair = 0
	badpair  = 0
	weirdexception = 0

	pairid, rockstara, rockstarb, massa, massb, radiusa, radiusb, sep0, onvel0, offvel0, sep1, onvel1, offvel1, sep2, onvel2, offvel2, sep3, onvel3, offvel3, sep4, onvel4, offvel4, sep5, onvel5, offvel5, sep6, onvel6, offvel6, sep7, onvel7, offvel7, sep8, onvel8, offvel8, sep9, onvel9, offvel9, sep10, onvel10, offvel10 = np.loadtxt('trees/late_treefile.csv', delimiter = ',', unpack = True)

	def minimacount(seplist, velylist, velzlist):
		number_of_minima = 0
		shrinking = 0
		growing   = 1
		past = shrinking
		for i in range(len(seplist[:-1])):

			if seplist[i+1] > seplist[i]:
				movement = growing
			else:
				movement = shrinking

			if movement == growing and past == shrinking:
				number_of_minima += 1

			past = movement

		if seplist[-1] < min(seplist[:-1]) and velzlist[-1] > 0:
			number_of_minima += 1

		return number_of_minima


	for a in range(len(pairid)):


		missingdata = False
		sep_list = [sep0[a], sep1[a], sep2[a], sep3[a], sep4[a], sep5[a], sep6[a], sep7[a], sep8[a], sep9[a], sep10[a]]
		vel_y_list = [offvel0[a], offvel1[a], offvel2[a], offvel3[a], offvel4[a], offvel5[a], offvel6[a], offvel7[a], offvel8[a], offvel9[a], offvel10[a]]
		vel_z_list = [onvel0[a], onvel1[a], onvel2[a], onvel3[a], onvel4[a], onvel5[a], onvel6[a], onvel7[a], onvel8[a], onvel9[a], onvel10[a]]

		for distance in sep_list:
			if distance > 50:
				missingdata = True
		if missingdata == True:
			weirdexception = weirdexception + 1
		
		if ( ( sep10[a] > min(sep_list[0:10]) ) or ( sep10[a] < min(sep_list[0:10]) and onvel10[a] > 0) ):
			#print minimacount(sep_list,vel_y_list, vel_z_list)
			og_pairs += 1
			if minimacount(sep_list, vel_y_list, vel_z_list) > 1:
				badpair += 1
			else:
				goodpair += 1



	print '\n'
	print 'weird exceptions: ' + str(weirdexception)
	print 'bad pairs: ' + str(badpair)
	print 'good pairs: ' + str(goodpair)
	print 'og pairs: ' + str(og_pairs)
	print 'max:' + str(len(pairid))
