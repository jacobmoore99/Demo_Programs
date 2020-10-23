import math

numbers = [5, 2, 8, 1, 3, 7]
print (numbers)
print (numbers[2])

for i in numbers:
	print(i, end=" ")
print ()

counter = 0
while counter < 10:
	print (counter)
	counter += 2 #same as counter = counter + 1

for counter in range (10, 0):
	print (counter)