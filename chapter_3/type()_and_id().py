x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))
print(id(x[0]))
print(id(y[0]))
if x[0] is y[0]:
    print("yup")
else:
    print("nope")
