import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import math
none = 0
outmass = []
outsep = []
outonvel= []
outoffvel= []
outrelvelangle= []
outprob= []
outmassratio= []
outvel= []
hpmass = []
hpsep = []
hponvel = []
hpoffvel = []
hprelvelangle = []
hpprob = []
hpmassratio = []
hpoutvel = []
hpvel = []



#this unpacks the data file
#173568 pairs
#pairid, haloa, halob, massa, massb, separation, onvel, offvel, relvelangle, prob = np.loadtxt('treefile.csv', delimiter = ',', unpack = True)
#pairid, massa, massb, separation, onvel, offvel, incoming, relvelangle, prob = np.loadtxt('cosmoallpairsafterpairsearch.csv', delimiter = ',', unpack = True)
massa, massb, separation, onvel, offvel, relvelangle, prob = np.loadtxt('rxcj1314.csv', delimiter = ',', unpack = True)


def vel(i):
    total = (math.sqrt(onvel[i]**2 + offvel[i]**2))/1000
    return(total)
    
    
#this looks for all of the outbound pairs and appends them to a different list to plot
for x in range(len(massa)):
    #these 2 lines can find all completely isolated pairs. Not much different than non isolated pairs
    #if haloa[x] not in halob and haloa[x] not in haloa[:x-1] and haloa[x] not in haloa[x+1:]:
        #if halob[x] not in haloa and halob[x] not in halob[:x-1] and halob[x] not in halob[x+1:]: 
    outmass.append((massa[x]+massb[x])/1e14)
    outsep.append(separation[x])
    outonvel.append(onvel[x])
    outoffvel.append(offvel[x])
    outrelvelangle.append(relvelangle[x])
    outprob.append(prob[x])
    if massa[x] > massb[x]:
        outmassratio.append(massa[x]/massb[x])
    else:
        outmassratio.append(massb[x]/massa[x])
    outvel.append(vel(x))

#this makes a smaller list of all the high probability pairs from the above list
for x in range(len(outprob)):
    if outprob[x] > 3700:
    	if separation[x] > 1:
    		print x
        hpmass.append((massa[x]+massb[x])/1e14)
        hpsep.append(separation[x])
        hponvel.append(onvel[x])
        hpoffvel.append(offvel[x])
        hprelvelangle.append(relvelangle[x])
        hpprob.append(prob[x])
        if massa[x] > massb[x]:
            hpmassratio.append(massa[x]/massb[x])
        else:
            hpmassratio.append(massb[x]/massa[x])
        hpvel.append(vel(x))
   
args = [outmass,outsep,outvel,outrelvelangle,outmassratio,outprob]
calls = ['Total Mass \n(10**14)','3D Separation \n(Mpc)','Velocity\n (1000km/s)','Relative \nVelocity Angle','Mass Ratio','Total Prob']

argshp = [hpmass, hpsep, hpvel, hprelvelangle, hpmassratio, hpprob]


#start the plots
fig, axes = plt.subplots(nrows = (len(args)), ncols = (len(args)))
fig.subplots_adjust(hspace=0, wspace = 0)

for c in range((len(args))):
    
    for r in range((len(args))):
        if (r == c):
        	if( r == (len(args)-1)):
        		axes[r,c].set_xlabel(calls[c])
        		axes[r,c].set_yticks([])
        		axes[r,c].hist(args[c], rwidth = 1, normed = True, weights = args[5])#1d histogram
        	else:
		        axes[r,c].hist(args[c], rwidth = 1, normed = True, weights = args[5])#1d histogram
		        axes[r,c].set_yticks([])
		        axes[r,c].set_xticks([])
        elif (r > c):
            axes[r,c].hist2d(args[c],args[r], bins = 30, cmap = 'binary', weights = args[5])#2d histogram across all arguments
            
            axes[r,c].scatter(argshp[c],argshp[r], c = 'b')#all high probability pairs are solid points
            
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
