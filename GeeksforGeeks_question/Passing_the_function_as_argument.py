def div1(text):
    return text.upper()


def div2(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("this is test")
    print(greeting)


greet(div1)
greet(div2)