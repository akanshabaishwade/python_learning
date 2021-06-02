capital = []
small = []
def var(num):
    print("inside var fuction num",num)
    print(capital)
    if True:# if num not in capital:
        capital.append(num)
        print(f"count of num:{num}",capital.count(num))
        print("=================")

        return True
    elif num > 2:

        print(capital.count(num))
        print('==============')

        return True
    else:

        return False
def var2(num):
    num += 2
    small.append(num)


print(var(10))
print(var(10))
print(var(12))
print(var(13))
print(var(10))
print(var(12))
print(var(13))

# print(capital)
# print(5)
# print(capital)
# print(var2(30))
# print(small)


