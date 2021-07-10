def main():
    kitten(Buffy='Mow', Zilla='grr', Angel='rawr')


def kitter(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('kitten {} say {}'.format(k, kwargs[k]))
    else:
        print('Mow.')


def main():
    x = dict(Buffy='Mow', Zilla='grr', Angel='rawr')
    kitten(**x)


def kitten(**kwargs):
    print(kwargs)
    if len(kwargs):
        for k in kwargs:
            print('kitten {} say {}'.format(k, kwargs[k]))
    else:
        print('Mow.')


if __name__ == '__main__':
    main()
