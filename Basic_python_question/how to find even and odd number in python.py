def even ():
    for count in range(100):
        if count % 2 == 0:
           print(count, "this is even number\n")
        else:
            print([count], "this is odd number\n")


print(even())
