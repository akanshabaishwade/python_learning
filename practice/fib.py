print("Fibonacci sequence:")
def add(first, Secound):
    turm = 100
    count = 0
    print(first)
    print(Secound)

    while count < turm:


        nth = first + Secound

        first = Secound

        Secound = nth
        count += 1
        if nth >= 1000:
            break

        print(nth)
add1 = add(35, 36)
add2 = add(70, 80)
main_siries = []

for i in range(len(add1)):
    main_siries.append( add1[i] + add2[i])
print(main_siries)


# main_siries = [add1[x] + add2[x] for x in range(len(add1))]
# print(main_siries)

# main_siries = list(map(add, add1, add2))
# print(main_siries)

