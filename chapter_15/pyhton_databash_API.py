# | |
#-----
# | |
#-----
# | |

for row in range(5):
    if row % 2 ==0 :
        current = (row/2)
        for column in range(5):
            if column% 2 == 0:
                current = (column/2)
                if column != 4:
                    print([row][column], end="")
                else:
                    print([row][column])
            else:
                print("|", end="")
    else:
        print("-----")