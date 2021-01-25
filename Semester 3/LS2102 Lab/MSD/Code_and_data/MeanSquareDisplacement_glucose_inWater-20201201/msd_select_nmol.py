import sys
import numpy as np

## STEP 1. Get the raw coordinates in an array of dimensions (nmol, 3*nfrm) for the chronological {x,y,z} of every molecule: 
infilepath = 'pureWat_310K_30mols_800ps.dat'
masterlist=np.loadtxt(infilepath)  #Inbuilt function in numpy which directly loads the textfile as a form of matrix :)
##print masterlist

### Get no. of molecules and no. of Frames directly from the data: 
dim = masterlist.shape
nmol=dim[0]
num_colmn=dim[1]
nfrm=num_colmn/3

print "\nNo. of Molecules = ",nmol,'\n'
print "\nNo. of Frames = ",nfrm,'\n'


## STEP 2. Enter information:
mm=raw_input("How many molecules would you like to calculate the MSD for? Enter:\n")
n_select=int(mm)
if n_select<=nmol:
        print '\n OK..\n'
else:
        sys.exit("No. of molecules exceeds no. for which data available!")


g=raw_input("\nEnter correlation time which is NOT greater than the No. of Frames:\n")
tcor=int(g)
if tcor<=nfrm:
	print '\n Please wait for the calculation..\n'
else:
	sys.exit("Use correct criteria for the number of frames!")



## STEP 3. Moving Time Origin formalism for calculating the Time Correlation Function:
###	  This step does the actual Mean Squared Displacement calculation.

tcf=[0.0]*nfrm
norm=[0]*nfrm

for m in range(0,n_select,1):

	for i in range(0,num_colmn,3):
		xi=masterlist[m][i]
		yi=masterlist[m][i+1]
		zi=masterlist[m][i+2]
		
		lastfrm = i+3*tcor

		if (lastfrm < num_colmn):
			for j in range(i,lastfrm,3):
				xj=masterlist[m][j]
				yj=masterlist[m][j+1]
				zj=masterlist[m][j+2]
				dt=(j-i)/3
				drSq=(xj-xi)**2+(yj-yi)**2+(zj-zi)**2
				tcf[dt] += drSq
				norm[dt] += 1

	curr_mol = m+1
	print 'Completed MSD calculation for molecule no.:  ', curr_mol, '\n'




## STEP 4: Normalize, ie.find the AVERAGE (delta_r)^2, or MSD, for each time interval:

#ps=raw_input("Enter the spacing between consecutive frames in picoseconds:")
g=raw_input('Enter output filepath and name:\n')
out_object=open(g,'w+')

for i in range(0,tcor):
	msd = tcf[i]/norm[i]
###	print 'Normalizing; time diff. = ',i
	out_object.write("%i %5.3f\n" % (i,msd))


out_object.close()
