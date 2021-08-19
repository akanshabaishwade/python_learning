# create a function with one argument
def deco(function):
    # create inner function "inner"
    def inner(x):
        #here difine variable 'num' equal too use function for closure 1st position and call_contents
        num = function.__closure__[0].cell_contents
        # Print num in srt and add
        print("I multiply with " + str(num))
        # return function with x
        return function(x)
    # return inner function
    return inner

# create another function 'make_multiplier_of' with n argument
def make_multiplier_of(n):
    # inner function 'multiply'
    def multiply(x):
        # return x multiply n
        return x*n

    return multiply

# create global variable 'multi7' and use function "make_multiplier_of" and give argument 10
multi7 = make_multiplier_of(10)
# create global variable for use @deco and The function inside the deco will be followed by "multi7"
multi7 = deco(multi7)
# here print multi7 with argument 5 means make_multiplier_of(10) = ans * 5
print(multi7(5))


@deco
def make_multiplier_of(n):
    def multiply(x):
        return x*n
    return multiply