def findFactors(Number):
	Number = int(input(" Please Enter any Number: "))
	Sum = 0
	for i in range(1, Number):
		if(Number % i == 0):
			print(str(i))

def sumFactors(list):
	Number = int(input(" Please Enter any Number: "))
	Sum = 0
	for i in range(1, Number):
		if(Number % i == 0):
			Sum = Sum + i
	print(str(Sum))

def printPerfectNumber(Number, Sum):
	if(Sum == Number):
		print(" %d " %Number)