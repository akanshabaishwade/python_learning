# create two variable x and y
x = 2
y = 20
#  here create two condition 1st is x grater then y, and 2ed is x less then y
x_greater_result = x > y
x_smaller_result = x < y
# here use function and say print with x grater and x smaller
print(f"x_greater_result:{x_greater_result}========x_smaller_result:{x_smaller_result}")
# use if statement for grater number
if x_greater_result:
    z = 112
    # use print satement and using format for print value of  x and y
    print("x>y:x is {} and y is {}".format(x, y))

    print('line2')
    print('line3')
elif x_smaller_result:
    # use print satement and using format for print value of  x and y
    print("x<y:x is {} and y is {}".format(x, y))

    z = 20
else:
    print("inside else")
    z = 50
print('line4')
print("something is else")
print("z is {}".format(z))
