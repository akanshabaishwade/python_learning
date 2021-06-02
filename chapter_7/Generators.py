def main():
    for i in inclusive_range(15, 55):
        print(i, end=' ')
    # print()
    # h = inclusive_range(50,70)
    # print(f"{h.__next__()}")
    # print(f"{h.__next__()}")
    # print(f"{h.__next__()}")
    # print(f"{h.__next__()}")
    # print(f"{h.__next__()}")
    # print(f"{h.__next__()}")
    # print(f"{h.__next__()}")
    # print(f"{h.__next__()}")


def inclusive_range(*args):
    numargs = len(args)
    start = 1
    step = 1
    print("my fun")

    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs} ')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 argument, got {numargs}')
    # generators
    i = start
    while i <= stop + 1:
        yield [78,56, i]
        i += step


if __name__ == '__main__':
    main()
