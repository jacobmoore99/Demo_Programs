import math

# Python Program to find Perfect Number between 1 to 1000

# Taking input from the user
Minimum = int(input("Please Enter any Minimum Value: "))
Maximum = int(input("Please Enter any Maximum Value: "))

# initialise sum


# Checking the Perfect Number
for Number in range(Minimum, Maximum - 1):
    Sum = 0
    for n in range(1, Number - 1):
        if(Number % n == 0):
            Sum = Sum + n       
    # display the result
    if(Sum == Number):
        print(" %d " %Number)