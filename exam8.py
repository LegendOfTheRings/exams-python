#Exercise #8

N = [0]*30
for i in range (30):
	N[i] = int(raw_input("Enter Number in between -30 and 30/n"))
	while ((N[i]<(-30)) | (N[i]>30)):
		N[i] = int(raw_input("Enter Number in between -30 and 30/n"))
for i in range(30):
	for j in range(30):
		for z in range(30):
			if (((N[i]+N[j]) and (N[j]+N[z]))==0)
				print ("Combination of numbers",i,j,z,"equals zero.")
				FLAG = true
if (!FLAG):
print ("No Valid Combination of Numbers was found.")
			