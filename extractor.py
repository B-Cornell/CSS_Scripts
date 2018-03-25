import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import math
id, rid1, rid2, massa, massb, rada, radb, separation, onvel, offvel, snap, smallsep = np.loadtxt('trees/treefile.csv', delimiter = ',', unpack = True)


def vel(i):
    total = (math.sqrt(onvel[i]**2 + offvel[i]**2))/1000
    return(total)

def relvel(i):
    angle = math.atan(abs(offvel[i]/onvel[i])) * (180.0 / 3.14159265)
    return angle

totalmass = []   
massratio = []
relvelangle = []
velocity = []
sep = []
closesep = []
snapnum = []
#this looks for all of the outbound pairs and appends them to a different list to plot
for x in range(len(massa)):
    if smallsep[x] < .35:
        totalmass.append((massa[x]+massb[x])/1e14)
        if massa[x] > massb[x]:
            massratio.append(massa[x]/massb[x])
        else:
            massratio.append(massb[x]/massa[x])
        velocity.append(vel(x))
        relvelangle.append(relvel(x))
        sep.append(separation[x])
        closesep.append(smallsep[x])
        snapnum.append(snap[x])

args = [totalmass, massratio, relvelangle, velocity, sep, closesep, snapnum]
calls = ["Total Mass  \n1E14 Msun", "Mass \nRatio", "Relative \nVelocity \nAngle", "Total \nVelocity \n(km/s)", "Separation \n(Mpc)", "Closest \nRecorded \nSeparation", "Snapshot \nNumber \nat Closest \nPass"]
#start the plots
fig, axes = plt.subplots(nrows = (len(args)), ncols = (len(args)))
fig.subplots_adjust(hspace=0, wspace = 0)

for c in range((len(args))):
    
    for r in range((len(args))):
        if (r == c):
        	if( r == (len(args)-1)):
        		axes[r,c].set_xlabel(calls[c])
        		axes[r,c].set_yticks([])
        		axes[r,c].hist(args[c], rwidth = 1, normed = True)#1d histogram
        	else:
		        axes[r,c].hist(args[c], rwidth = 1, normed = True)#1d histogram
		        axes[r,c].set_yticks([])
		        axes[r,c].set_xticks([])
        elif (r > c):
            axes[r,c].hist2d(args[c],args[r], bins = 30, cmap = 'binary')#2d histogram across all arguments
            
            #axes[r,c].scatter(argshp[c],argshp[r], c = 'b')#all high probability pairs are solid points
            
            if(r == (len(args)-1)):
                axes[r,c].set_xlabel(calls[c])
            else:
                axes[r,c].set_xticks([])
            if(c == 0):
                axes[r,c].set_ylabel(calls[r])
            else:
                axes[r,c].set_yticks([])
        else:
            axes[r,c].axis('off')
            

plt.show()

totalmass = []   
massratio = []
relvelangle = []
velocity = []
sep = []
closesep = []
snapnum = []
#this looks for all of the outbound pairs and appends them to a different list to plot
for x in range(len(massa)):
    if smallsep[x] < .7:
        totalmass.append((massa[x]+massb[x])/1e14)
        if massa[x] > massb[x]:
            massratio.append(massa[x]/massb[x])
        else:
            massratio.append(massb[x]/massa[x])
        velocity.append(vel(x))
        relvelangle.append(relvel(x))
        sep.append(separation[x])
        closesep.append(smallsep[x])
        snapnum.append(snap[x])

args = [totalmass, massratio, relvelangle, velocity, sep, closesep, snapnum]
calls = ["Total Mass  \n1E14 Msun", "Mass \nRatio", "Relative \nVelocity \nAngle", "Total \nVelocity \n(km/s)", "Separation \n(Mpc)", "Closest \nRecorded \nSeparation", "Snapshot \nNumber \nat Closest \nPass"]

#start the plots
fig, axes = plt.subplots(nrows = (len(args)), ncols = (len(args)))
fig.subplots_adjust(hspace=0, wspace = 0)

for c in range((len(args))):
    
    for r in range((len(args))):
        if (r == c):
        	if( r == (len(args)-1)):
        		axes[r,c].set_xlabel(calls[c])
        		axes[r,c].set_yticks([])
        		axes[r,c].hist(args[c], rwidth = 1, normed = True)#1d histogram
        	else:
		        axes[r,c].hist(args[c], rwidth = 1, normed = True)#1d histogram
		        axes[r,c].set_yticks([])
		        axes[r,c].set_xticks([])
        elif (r > c):
            axes[r,c].hist2d(args[c],args[r], bins = 30, cmap = 'binary')#2d histogram across all arguments
            
            #axes[r,c].scatter(argshp[c],argshp[r], c = 'b')#all high probability pairs are solid points
            
            if(r == (len(args)-1)):
                axes[r,c].set_xlabel(calls[c])
            else:
                axes[r,c].set_xticks([])
            if(c == 0):
                axes[r,c].set_ylabel(calls[r])
            else:
                axes[r,c].set_yticks([])
        else:
            axes[r,c].axis('off')
            

plt.show()

