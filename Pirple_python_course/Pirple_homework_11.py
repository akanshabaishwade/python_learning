number1 =input("Enter 1st number:- ")
number2 =input("Enter 2st number:- ")
try:
    print("sum of this number is ",
          int(number1) + int(number2))
except Exception as e:
    print(e)


print("this is your answer")