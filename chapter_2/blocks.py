x = 2
y = 20
x_greater_result = x > y
x_smaller_result = x < y
print(f"x_greater_result:{x_greater_result}========x_smaller_result:{x_smaller_result}")
if x_greater_result:
    z = 112
    print("x>y:x is {} and y is {}".format(x, y))
    print('line2')
    print('line3')
elif x_smaller_result:
    print("x<y:x is {} and y is {}".format(x, y))
    z = 20
else:
    print("inside else")
    z = 50
print('line4')
print("something is else")
print("z is {}".format(z))
