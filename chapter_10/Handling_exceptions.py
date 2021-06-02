def main():
    try:

       x = 'job'
    except ValueError:
        print('i caught a vlaueerror')

    except ZeroDivisionError:
        print('''don't divide by zero''')

    else:
        print('good job!')

        print(x)




if __name__ == '__main__':
     main()