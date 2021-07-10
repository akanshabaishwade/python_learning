nayra = 10
Top_print = "python"

for i in range(1, nayra+1):
    print(Top_print*i)
for i in range(nayra, 0, -1):
    print(Top_print*i)

rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of column:"))
k = 2 * rows - 2  # It is used for number of spaces
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2   # decrement k value after each iteration
    for j in range(0, i + 1):
        print("@ ", end="")  # printing @
    print(".....")
for i in range(rows,0, -1):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i):
        print("@ ", end="")  # printing @
    print(".....")
print(i)
