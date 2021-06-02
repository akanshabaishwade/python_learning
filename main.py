a = "hello"
b = "world"
c = a + " " + b
print(c)
age = "49"
txt = "my name is anshu, i am " + age
print(txt)
age = 40
txt = "my name is anshu, and  i am {}"
print(txt.format(age))
age = 68
a = "my name is john, and my age {}"
print(a.format(age))
quantity = 9990
itemno = 79489
price = 89
myorder = "i want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#fix this problem
txt = "we are the so-called \"vikings\" from the north"
print(txt)
txt = 'it\'s alright'
print(txt)
txt = "this will insert one \\ (anshu)."
print(txt)
txt = "anshu is a superb investor\nyou are pro in stock market"
print(txt)
# carriage return means bich se cut krk aage ka likna ho to.....
txt = "hello\rworld"
print(txt)
txt = "hello\tworld"
print(txt)
print('''hello my friends what are you doing guys follow me and subscribe my channel''')
#from playsound import playsound
#playsound('ghumighumi.mp3')
import os
print(os.listdir())
# logical operators
bool1 = True
bool2 = False
print("the value of bool1 and bool2 is", (bool1 and bool2))
print(4+3)
a = 32
b = 33
print(a * b)
a = int(input("Enter first number :   "))
b = input("Enter second number :  ")
avg = (a + int(b))/2
print("the value of average  is")


