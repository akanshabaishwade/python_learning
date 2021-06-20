def bord(a, b):
    for row in a:
        for i in range (1, b+1):
           print(row*i, end=" ")
        print("")

bord("akansha", 5)
