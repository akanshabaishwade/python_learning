' a. To check if the year is a Leap year or not '

def Check_Leap(year):
    #  Checking if the given year is leap year
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            # Else it is not a leap year
            else:
                print("{0} is not a leap year".format(year))
        # Else it is not a leap year
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
#  Taking an input year from user
Year = int(input("Enter Year : "))
# Printing result
Check_Leap(Year)

' b. check whether a number is Prime or not '


#import math
from math import sqrt
# n is the number to be check whether it is prime or not
n = 1

# no lets check from 2 to sqrt(n)
# if we found any facto then we can print as not a prime number

# this flag maintains status whether the n is prime or not
prime_flag = 0
#  if n is grater then 1 then
if(n > 1):
	for i in range(2, int(sqrt(n)) + 1):
		if (n % i == 0):
			prime_flag = 1
			break
	if (prime_flag == 0):
		print("true")
	else:
		print("false")
else:
	print("false")
