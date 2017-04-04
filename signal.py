import sys
from os import getcwd
from os import listdir
from os.path import isfile,join
import subprocess

def runbwtool():
	mypath = getcwd()
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	onlybigwig = [name for name in onlyfiles if name.endswith((".bigWig"))]
	for i in onlybigwig:
		a = 0
		subprocess.Popen('bwtool dist '+i+' output'+a+'.txt', shell = True)
		a= a+1
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	onlytxt = [name for name in onlyfiles if name.endswith((".bigWig"))]
	for i in onlytxt:
		file_object = open(mypath+i ,'r')
		distribution = file_object.readlines()
		distr= []
		for line in distribution:
			line = line.strip('\n')
			line = line.split('\t')
			distr.append(line)
		bigframe =int( input("Enter size of bigger frame:\t"))
		smallframe =int( input("Enter size of smaller frame:\t"))
		distribution =[]
		subsetsBig=[]
		subsetsSmall=[]
		for i in range(len( distr)):
			if (i+bigframe) <= (len(distr)-1):
				subsetsBig.append(distr[i:bigframe+i])
		for i in subsetsBig:
			middleBig = (bigframe//2)-1
			middleSmall = (smallframe//2)
			subsetsSmall.append(i[(middleBig-middleSmall):( (middleBig-middleSmall)+smallframe )
		result =[]
		for i in range(len(subsetsBig)):
			itern =[]
			if mean(subsetsBig[i]) < mean(subsetsSmall[i]):
				itern = [1,mean(subsetsSmall[i]), mean(subsetsBig[i]), mean(subsetsBig[i])/mean(subsetsSmall[i])*100]
			else:
				itern = [0,mean(subsetsSmall[i]), mean(subsetsBig[i]), mean(subsetsBig[i])/mean(subsetsSmall[i])*100]
			result.append(itern)
		outputName = input("Enter output name without extension \t")
		file_object2 = open (mypath+outputName, 'w')
		for i in result:
			file_object2.write(i)

if __name__ == "__main__":
	runbwtool()
