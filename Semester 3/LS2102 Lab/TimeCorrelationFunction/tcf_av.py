# Import Modules

import numpy as np
import sys


# Extract Raw Coordinates

skipFrm = 0
increment = skipFrm+1
inFile = sys.argv[-1]
masterList = np.loadtxt(inFile)                 # Array of ordered coordinates
totFrm = len(masterList)                        # No. of total frames
nFrm = int(totFrm/increment)                      # No. of used frames
print("\nNo. of frames = %d\n"%(nFrm))


# User Input

tCor = int(input("Enter correlation time (not > number of frames): "))
if tCor<=nFrm:
    print("\nPlease wait for the calculation...\n")
else:
    sys.exit("\nUse proper criteria for the correlation time value!\n")

# find the Mean
totVal = 0.0
for f in range(0, totFrm, increment):
	totVal += masterList[f]

mean = totVal/(1.0*totFrm)


# Moving Time Origin for calculating the Time Correlation Function 

tcF = [0.0]*tCor
norm = [0]*tCor
for i in range(0, totFrm, increment):
    lastFrm = i+increment*tCor
    if (lastFrm < totFrm):
        for j in range(i, lastFrm, increment):
            dVal_i=masterList[i] - mean
            dVal_j=masterList[j] - mean
            print(dVal_i,dVal_j)
            dt=int((j-i)/increment)
            drSq=np.sum((dVal_i*dVal_j))	
#           drSq=np.sum((XYZ_i-XYZ_j)**2)
            tcF[dt]+=drSq
            norm[dt]+=1

    print("Complete Frm %d"%(int(i/increment)+1))


# Find the TCF for each time interval

outFile = inFile[:-4]+'_tcf.dat'
norm = np.trim_zeros(np.array(norm))
tcF = tcF[-len(norm):]
tcf_norm = tcF/norm
tcf_norm = tcf_norm/(tcf_norm[0])
dT = np.linspace(0,tCor,len(norm),dtype=int)
outData = np.array([dT,tcf_norm]).T
np.savetxt(outFile,outData,fmt='%.10f')
