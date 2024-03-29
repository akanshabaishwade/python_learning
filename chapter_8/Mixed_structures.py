dlevel = 0

def main():
    r = range(11)
    l = [1, 'two', 3, {'4':'four'}, 5]
    t = ('one', 'two', 'none', 'four', 'five')
    s = set("it's a bird! It's a plane! It's Superman! ")
    d = dict(one=r, two=l, three=s)
    mixed = [l, r, s, d, t]
    disp(mixed)

def disp(o):
    global dlevel

    dlevel += 1
    if isinstance(o, list): print_list(o)
    elif isinstance(o, range): print_list(o)
    elif isinstance(o, tuple): print_list(o)
    elif isinstance(o, set): print_list(o)
    elif isinstance(o, dict): print_list(o)
    elif o is None: print('Nada', end = '', flush=True)
    else: print(repr(o), end=' ', flush=True)
    dlevel -= 1

    if dlevel<= 1: print()

def print_list(o):
    print('[', end=' ')
    for x in o: disp(x)
    print(']', end = ' ', flush=True)


def print_tuple(o):
    print('(', end=' ')
    for x in o: disp(x)
    print(')', end = ' ', flush=True)


def print_set(o):
    print('{', end=' ')
    for x in o: disp(x)
    print('}', end = ' ', flush=True)


def print_dict(o):
    print('{', end=' ')
    for k,v in o.items():
        print(k, end=': ')
        disp(v)
    print('}', end = ' ', flush=True)

if __name__ == "__main__":
    main()


