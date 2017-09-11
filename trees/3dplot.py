import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D



rowid, haloa, snapnum, x, y, z, vx, vy, vz, mass, radius, depthfirstid= np.loadtxt('capaps9omg.csv', delimiter = ',', unpack = True, skiprows = 130)
for i in range(len(mass)):
    mass[i] = mass[i]/1E14

    
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')

ax.scatter(x,y,z, c = snapnum)
plt.show()
