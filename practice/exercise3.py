" how to write a table from (1 to i) "

for row in range(1, 10):
    for column in range(1, 10):
        print(row*column, end=" ")
    print("\n")