def drafield(field):
    for row in range(5): # 0, 1, 2 , 3, 4

        if row % 2 == 0: # 0, 2, 4
            practicalrow = int(row/2) # 0, 1, 2
            for column in range(5): # 0, 1, 2 , 3, 4
               if column % 2 == 0: # 0, 2 , 4
                   practicalcolum = int(column/2) # 0, 1, 2
                   if column != 4:
                       print(field[practicalcolum][practicalrow], end="")
                   else:
                       print(field[practicalcolum][practicalrow])
               else:
                   print("|", end="")

        else:
            print("------")
player = 1
currentfield = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# print(currentfield)
while(True):
    print("players turn: ", player)
    row_name, column_name = [int(x) for x in input("please Enter the Row,Column\n").split(",")]

    if player == 1:

        if  currentfield[column_name][row_name] == " ":
            currentfield[column_name][row_name] = "X"
            player = 2

    else:

        if  currentfield[column_name][row_name] == " ":
            currentfield[column_name][row_name] = "O"
            player = 1
    drafield(currentfield)


# print(drafield())

