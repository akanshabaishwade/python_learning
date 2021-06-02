def main():
    seq = range(11)
    seq2 = [x * 3 for x in seq]
    seq3 = [(x, x**2) for x in seq]
    print_list(seq)
    print('==============')
    print_list(seq2)
    print('==============')
    print_list(seq3)

def print_list(o):
    for x in o:
        print(x, end = ' ')
        print()

if __name__ == '__main__':
    main()