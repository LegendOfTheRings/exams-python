#Exercise #13

def countRec(n, s) :
	if (n == 0) :
		return (s == 0)
	if (s == 0) :
		return 1
	answer = 0
	#for i in range(n): (χρησιμοποιώ αλγόρυθμο φυσαλίδας για να κάνω έλεγχο αύξουσας σειράς)
	#	for j in range(i,-1):
	#		if (n[j-1] > n[j]):
	#		else:
	#			FLAG = 0
	#if (FLAG==1):
	for i in range(0, 10) :
		if (s-i >= 0) :
			answer = answer + countRec(n-1, s-i)
	return answer
def finalCount(n, s) :
	answer = 0
	#for i in range(n): (χρησιμοποιώ αλγόρυθμο φυσαλίδας για να κάνω έλεγχο αύξουσας σειράς)
	#	for j in range(i,-1):
	#		if (n[j-1] > n[j]):
	#		else:
	#			FLAG = 0
	#if (FLAG==1):
	for i in range(1, 10) :
		if (s-i >= 0) :
			answer = answer + countRec(n-1, s-i)
	return answer
n = int(raw_input("Give Number Of Digits."))
s = int(raw_input("Give Sum Of Digits."))
print(finalCount(n, s))