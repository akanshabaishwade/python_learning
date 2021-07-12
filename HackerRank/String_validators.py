
if __name__ == '__main__':
    a = str(input())
    isalnum = a.isalnum()
    isalpha = a.isalpha()
    isdigit = a.isdigit()
    islower = a.islower()
    isupper = a.isupper()

    print(any(c.isalnum() for c in a ))
    print(any(c.isalpha() for c in a))
    print(any(c.isdigit() for c in a))
    print(any(c.islower() for c in a))
    print(any(c.isupper() for c in a))
