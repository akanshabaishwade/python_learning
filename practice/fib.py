print("Fibonacci sequence:")

def add(first, Secound):
    fib_series = list()
    turm = 100
    count = 0
    fib_series.append(first)
    fib_series.append(Secound)


    while count < turm:


        nth = first * Secound

        first = Secound

        Secound = nth
        count += 1
        if nth >= 1000:
            break

        fib_series.append(nth)
    return fib_series
add1 = add(35, 36)
add2 = add(70, 80)
add3 = add(11, 16)
main_siries = []
print(add1)
print(add2)
print(add3)

for i in range(len(add1)-1):
    main_siries.append(add1[i] + add2[i] + add3[i])
print(main_siries)
