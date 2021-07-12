number = int(input())

l = len("{0:b}".format(number))

def print_formatted(number):
    for i in range(1, number):
        # print(i, oct(i).replace("0o", ""), hex(i).replace("0x", ""), len(bin(i).replace("0b", "")))
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=l))


print_formatted(number)
