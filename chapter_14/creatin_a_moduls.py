import saytime
def main():
    st = saytime.saytime()
    print('\nnumbers test: ')
    list = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    for l in list :
        st.number(l)
        print(l, st.numwords())


    print('\ntime test:')

if __name__ == '__main__': main()