def deco(func):
    def inner(x):
        num = func.__closure__[0].cell_contents
        print("I multiply with " + str(num))
        return func(x)
    return inner


def make_multiplier_of(n):
    def multiply(x):
        return x*n
    return multiply


multi7 = make_multiplier_of(7)
multi7 = deco(multi7)
print(multi7(5))

@deco
def make_multiplier_of(n):
    def multiply(x):
        return x*n
    return multiply