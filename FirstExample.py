import math

number1 = input ("Enter a value: ")
number2 = input ('Enter another value: ')
number1 = int (number1)
number2 = int (number2)

answer = number1 * number2
print (answer)

answer = number1 / number2
print (answer)
print (math.floor(answer))
print (math.ceil(answer))
print (math.trunc(answer))

answer = number1 // number2
print (answer)

answer = number1 % number2
print (answer)

if number1 % number2 == 0:
	print (str(number1) + ' is a multiple of ' + str(number2))
elif number2 % number1 == 0:
	print (str(number2) + ' is a multiple of ' + str(number1))
else:
	print ("Neither of these is a multiple of the other.")