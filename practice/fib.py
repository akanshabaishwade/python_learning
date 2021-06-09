turm = 100
first, Secound = 35, 36
count = 0


print("Fibonacci sequence:")
print(first)
print(Secound)
while count < turm:

    nth = first + Secound

    first = Secound
    Secound = nth
    count += 1
    if nth >= 1000:
        break
    # i = d.append(nterms)
    print(nth)


