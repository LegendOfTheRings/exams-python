#Exercise #1

for i in range(100):
	for j in range(5):
		N[i,j]=raw_input("Give a number in between 1 and 80\n")
		FLAG = 0
		while (FLAG==0):
		if N[i,j]>=1 and N[i,j]<=80
			FLAG = 1
		else:
			print ("Give valid number in between 1 and 80")
Sum = 0
for k in range(1000):
	for j in range(5):
		import random
		a = range(1,80)
		for i in xrange(5):
			b = a[random.randint(0,len(a)-i)]
			a.remove(b)
			Bingo[j] = b
			for i in range(100):
				if (N[i,j]==Bingo[j]):
					break
				else:
					Sum = Sum + 1
MO = Sum/1000
print ("Mesos Oros", MO)