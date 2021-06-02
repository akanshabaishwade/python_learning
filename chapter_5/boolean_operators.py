a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if y in x:
    print('expression is True')
else:
    print('expression is false')


x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if y in x[0]:
    print('expression is True')
else:
    print('expression is false')


x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if y is not x[0]:
    print('expression is True')
else:
    print('expression is false')


x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if 'bunny' in x[1]:
    print('expression is True')
else:
    print('expression is false')


x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if y is x[0]:
    print('expression is True')
else:
    print('expression is false')
print(id(x[0]))
print(id(y))