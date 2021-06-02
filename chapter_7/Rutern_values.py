def main():
    x = kitten()
    print(type(x), x)


def kitten():
    print('Meow.')
    return 57

main()


def main2():
    x = kitten2()
    print(type(x), x)


def kitten2():
    print('Meow.')
    return [34, 98, 39, 22]


main2()


def main3():
    x = kitten3()
    print(type(x), x)


def kitten3():
    print('Meow.')
    return dict(x=34, y=33, z=20)


if __name__ == '__main__':
    main3()



