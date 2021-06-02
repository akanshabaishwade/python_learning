def main():
    kitten(Buffy='Mouw', Zilla='grr', Angel='rawr')


def kitter(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('kitten {} say {}'.format(k, kwargs[k]))
    else:
        print('Mouw.')


def main():
    x = dict(Buffy='Mouw', Zilla='grr', Angel='rawr')
    kitten(**x)


def kitten(**kwargs):
    print(kwargs)
    if len(kwargs):
        for k in kwargs:
            print('kitten {} say {}'.format(k, kwargs[k]))
    else:
        print('Mouw.')


if __name__ == '__main__':
    main()
