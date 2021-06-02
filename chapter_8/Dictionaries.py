def main():
    animals = {'kitten': 'meow', 'pully': 'ruff!', 'lion': 'ogrerr'}
    print_dict(animals)
    for k,v  in animals.items(): print((f'{k}: {v}'))

def print_dict(o):
    for x in o:
        print(f'{x}:{o[x]}')
main()



print('==============')

def main2():
    animals = dict(kitten = 'helloo',  pully = 'ruff!', lion = 'ogrerr')

    animals['lion'] = 'my mom is lion'
    for v in animals.values(): print(v)
    print_dict(animals)



def print_dict(o):
    for x in o:
        print(f'{x}:{o[x]}')
main2()
