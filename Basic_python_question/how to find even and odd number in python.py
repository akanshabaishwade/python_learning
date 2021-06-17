list = []
limit = 100
def even ():
    for count in range(100):
        if count % 2 == 0:
            print(count)
            if count> limit:
                break
        list.append(count)



print(list)