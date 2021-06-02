def main():
    kitten(5, 6, 7)

def kitten(a, b, c):
    print('Mouw.')
    print(a, b, c)


if __name__ == '__main__':
    main()



def main():
    kitten(5, 6, )

def kitten(a, b, c = 0):
    print('Mouw.')
    print(a, b, c)


if __name__ == '__main__':
    main()



def main():
    x = 5
    print(id(x))
    kitten(x)
    print(f'in main: x is {x} ')

def kitten(a):
    a = [9]
    print(id(a))

    print('Mouw.')
    print(a)


if __name__ == '__main__':
    main()

