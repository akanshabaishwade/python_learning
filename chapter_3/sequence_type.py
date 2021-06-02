x = [1, 2, 3, 4, 5]
for i in x:
    print('is is {}'.format(i))
print("=====")
x = range(10)
for i in x:
    print('is is {}'.format(i))
x = list(range(10))
x[2] = 8
print("=============")
for i in x:                   # dictionary
    print('is is {}'.format(i))
print("==========")
x = {'one': 1, 'two': 2, 'three': 3}
for k,v in x .items():
    print(f'k:{k}, v: {v}')




