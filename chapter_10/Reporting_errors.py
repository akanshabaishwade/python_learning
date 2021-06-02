def including_range(*args):
    numbers = len(args)
    stat = 0
    stop = 1


    if numbers < 1:
        raise TypeError(f'expected at laest one argument, got {numbers}')
    elif numbers == 1:
        stop = args[0]
    elif numbers == 2:
        (start, stop) = args
    elif numbers == 3:
        (start, stop, step) = args

    else: raise TypeError(f'expected at least 3 argument, got {numbers}')


    def main():
        for i in inclusive_range(25):
            print(i, end=' ')
        print()


if __name__ == '__main__': main()
