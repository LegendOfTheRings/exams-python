#Exercise #7

Y = []
Y[0] = raw_input("Give Year/n")
for i in range(10):
	Y[i] = (Y[i]+1)
Months[0] = 31
Months[2] = 31
Months[3] = 30
Months[4] = 31
Months[5] = 30
Months[6] = 31
Months[7] = 31
Months[8] = 30
Months[9] = 31
Months[10] = 30
Months[11] = 31
Left = 0
S = 0
FLAG = 1
D = raw_input("Give Day/n")
d = raw_input("Give date/n")
M = raw_input("Give Month/n")
for i in range(10): # 10 years
	if ((((Y[i]%4)==0) | (Y[i]%100)==0) and(Y[i]%400)!=0): # disekto h oxi disekto etos
		Months[1] = 29
	else:
		Months[1] = 28
	for z in range(12) #12 months
		if (FLAG==1):
			z = M
		for x in range(Months[z],7):
			if (FLAG==1):
				x = d
			if (Left!=0):
				x = (x-7-Left)
				Left = 0
				Continue
			if ((x+7)>Months[z]):
				Left = (Months[z]-x)
			else:
				Left = 0
			FLAG = 0
			if (x==8):
				S = S+1
			if ((i==9) and (z>=M):
				Break
print ("There will be ",S,"Mondays with a date of 8 within the next 10 years.")