def playing_board(rows, columns):
    maximum_columns = 100
    maximum_rows = 150
    if columns <= maximum_columns and rows <= maximum_rows:

        for row in range(rows):
            if row % 2 == 0:
                for board in range(1, columns):
                    if board % 2 == 1:
                        if board != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        return True

    else:

        reason = " "
        if columns > maximum_columns and rows > maximum_rows:
            reason = "columns and rows"
        elif columns > maximum_columns:
            reason += "columns"
        elif rows > maximum_rows:
            reason += "rows"
        print("Sorry, cannot create the board, too many".format(reason))
        return False

playing_board(100,100)