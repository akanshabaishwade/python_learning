def main():
    x = ('meow', 'grr', 'purr')    # style one
    kitten(*x)


def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('meow.')


if __name__ == '__main__':
    main()

print("==============================")

def main():

    kitten('meow', 'grr', 'purr')  # style two


def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('meow.')


if __name__ == '__main__':
    main()