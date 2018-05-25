import numpy as np
import math
import sys

massa, massb, separation, onvel, offvel, sep9, onvel9, offvel9, sep10, onvel10, offvel10, sep11, onvel11, offvel11, sep12, onvel12, offvel12, sep13, onvel13, offvel13, sep14, onvel14, offvel14, sep15, onvel15, offvel15, sep16, onvel16, offvel16, sep17, onvel17, offvel17, sep18, onvel18, offvel18, sep19, onvel19, offvel19, sep20, onvel20, offvel20, sep21, onvel21, offvel21, sep22, onvel22, offvel22, sep23, onvel23, offvel23, sep24, onvel24, offvel24, sep25, onvel25, offvel25, sep26, onvel26, offvel26, sep27, onvel27, offvel27, sep28, onvel28, offvel28, sep29, onvel29, offvel29, sep30, onvel30, offvel30, sep31, onvel31, offvel31, sep32, onvel32, offvel32, sep33, onvel33, offvel33, sep34, onvel34, offvel34, sep35, onvel35, offvel35, sep36, onvel36, offvel36, sep37, onvel37, offvel37, sep38, onvel38, offvel38, sep39, onvel39, offvel39, sep40, onvel40, offvel40, sep41, onvel41, offvel41, sep42, onvel42, offvel42, sep43, onvel43, offvel43, sep44, onvel44, offvel44, sep45, onvel45, offvel45, sep46, onvel46, offvel46, sep47, onvel47, offvel47, sep48, onvel48, offvel48, sep49, onvel49, offvel49, sep50, onvel50, offvel50, sep51, onvel51, offvel51, sep52, onvel52, offvel52, sep53, onvel53, offvel53, sep54, onvel54, offvel54, sep55, onvel55, offvel55, sep56, onvel56, offvel56, sep57, onvel57, offvel57, sep58, onvel58, offvel58, sep59, onvel59, offvel59, sep60, onvel60, offvel60, sep61, onvel61, offvel61, sep62, onvel62, offvel62, sep63, onvel63, offvel63, sep64, onvel64, offvel64, sep65, onvel65, offvel65, sep66, onvel66, offvel66, sep67, onvel67, offvel67, sep68, onvel68, offvel68, sep69, onvel69, offvel69, sep70, onvel70, offvel70, sep71, onvel71, offvel71, sep72, onvel72, offvel72, sep73, onvel73, offvel73, sep74, onvel74, offvel74, sep75, onvel75, offvel75, sep76, onvel76, offvel76 = np.loadtxt('full_tree_data_77.txt', delimiter = ',', unpack = True, skiprows = 1)
#

count = 0
f = open('final_data_77.txt', 'w')
for i in range(len(massa)):
    early = 0
    late = 0
    passes = 0
    seplist = []
    offvellist = []
    onvellist = []

    initseplist = [sep9[i], sep10[i], sep11[i], sep12[i], sep13[i], sep14[i], sep15[i], sep16[i], sep17[i], sep18[i], sep19[i], sep20[i], sep21[i], sep22[i], sep23[i], sep24[i], sep25[i], sep26[i], sep27[i], sep28[i], sep29[i], sep30[i], sep31[i], sep32[i], sep33[i], sep34[i], sep35[i], sep36[i], sep37[i], sep38[i], sep39[i], sep40[i], sep41[i], sep42[i], sep43[i], sep44[i], sep45[i], sep46[i], sep47[i], sep48[i], sep49[i], sep50[i], sep51[i], sep52[i], sep53[i], sep54[i], sep55[i], sep56[i], sep57[i], sep58[i], sep59[i], sep60[i], sep61[i], sep62[i], sep63[i], sep64[i], sep65[i], sep66[i], sep67[i], sep68[i], sep69[i], sep70[i], sep71[i], sep72[i], sep73[i], sep74[i], sep75[i], sep76[i], separation[i]]

    initoffvel = [offvel9[i], offvel10[i], offvel11[i], offvel12[i], offvel13[i], offvel14[i], offvel15[i], offvel16[i], offvel17[i], offvel18[i], offvel19[i], offvel20[i], offvel21[i], offvel22[i], offvel23[i], offvel24[i], offvel25[i], offvel26[i], offvel27[i], offvel28[i], offvel29[i], offvel30[i], offvel31[i], offvel32[i], offvel33[i], offvel34[i], offvel35[i], offvel36[i], offvel37[i], offvel38[i], offvel39[i], offvel40[i], offvel41[i], offvel42[i], offvel43[i], offvel44[i], offvel45[i], offvel46[i], offvel47[i], offvel48[i], offvel49[i], offvel50[i], offvel51[i], offvel52[i], offvel53[i], offvel54[i], offvel55[i], offvel56[i], offvel57[i], offvel58[i], offvel59[i], offvel60[i], offvel61[i], offvel62[i], offvel63[i], offvel64[i], offvel65[i], offvel66[i], offvel67[i], offvel68[i], offvel69[i], offvel70[i], offvel71[i], offvel72[i], offvel73[i], offvel74[i], offvel75[i], offvel76[i], offvel[i]]

    initonvel = [onvel9[i], onvel10[i], onvel11[i], onvel12[i], onvel13[i], onvel14[i], onvel15[i], onvel16[i], onvel17[i], onvel18[i], onvel19[i], onvel20[i], onvel21[i], onvel22[i], onvel23[i], onvel24[i], onvel25[i], onvel26[i], onvel27[i], onvel28[i], onvel29[i], onvel30[i], onvel31[i], onvel32[i], onvel33[i], onvel34[i], onvel35[i], onvel36[i], onvel37[i], onvel38[i], onvel39[i], onvel40[i], onvel41[i], onvel42[i], onvel43[i], onvel44[i], onvel45[i], onvel46[i], onvel47[i], onvel48[i], onvel49[i], onvel50[i], onvel51[i], onvel52[i], onvel53[i], onvel54[i], onvel55[i], onvel56[i], onvel57[i], onvel58[i], onvel59[i], onvel60[i], onvel61[i], onvel62[i], onvel63[i], onvel64[i], onvel65[i], onvel66[i], onvel67[i], onvel68[i], onvel69[i], onvel70[i], onvel71[i], onvel72[i], onvel73[i], onvel74[i], onvel75[i], onvel76[i], onvel[i]]

    for dist in range(len(initseplist)):
        if initseplist[dist] != 0 and initoffvel[dist] != 0 and initonvel[dist] != 0:
            seplist.append(initseplist[dist])
            offvellist.append(initoffvel[dist])
            onvellist.append(initonvel[dist])

    for time in range(1,len(seplist)-1):
        if seplist[time] < seplist[time+1] and seplist[time] < seplist[time-1] and seplist[time] < .5:
            pass_rel_vel_angle = math.atan(abs(offvellist[time]/onvellist[time]))
            pericenter = seplist[time]*math.sin(pass_rel_vel_angle)
            passes += 1
            early += 1
    if len(seplist) > 3:
        if seplist[-1] < seplist[-2] and seplist[-1] < .5 and onvel[i] > 0:
            pass_rel_vel_angle = math.atan(abs(offvel[i]/onvel[i]))
            pericenter = separation[i]*math.sin(pass_rel_vel_angle)
            passes += 1
            late += 1

    if passes == 1:
        count += 1
        f.write(str(massa[i]) + ', ' + str(massb[i]) + ', ' + str(separation[i]) + ', ' + str(onvel[i]) + ', ' + str(offvel[i]) + ', ' + str(pericenter) + '\n')
        #write out mass, velocities, pericenter, separation
        #print ''


print count
print len(massa)
