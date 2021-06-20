# for colour in python use termcolor and import colored cprint
from termcolor import colored, cprint

# create Empty list for fill all the player action
fields = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
          [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
          [" ", " ", " ", " ", " ", " ", " "]]

# create function for designed outer tik tak toe designed
def draw_board(fields):
    # use for loop and take range 12 because we create game for 7 column and 6 row
    for row in range(13):
        # use if statement for only even number enter this loop
        if row % 2 == 0:
            # if number is even so, current_row is in int and divided by 2 because we need to row for feel the term for row
            current_row = int(row / 2)
            # use again for loop for column range of 13
            for column in range(13):
                # use if statement for make column
                if column % 2 == 0:
                    # if number is even so current_column is deviation of 2 in int form
                    current_column = int(column / 2)
                    # from termcolor for colour
                    color = "white"
                    # place in current_column current_row put X, in colour red
                    if fields[current_column][current_row] == "X":
                        color = "red"
                    #     create new variable for current_column current_row for bold the colour from colored
                    main = colored(fields[current_column][current_row], color, attrs=['bold'])
                    # if column is not equal to 12 so print main this if for remove 12
                    if column != 12:

                        print(main, end="")
                    else:
                        print(main)
                else:
                    print("|", end="")
        else:
            print("-------------")
    print("\n")

# create new function (updateBoard) with 1 condition (run num to player)
def updateBoard(num, player):
    column = fields[num]
    index = ""
    reversed_column = column[::-1]
    for row in reversed_column:
        if row == " ":
            index = reversed_column.index(row)
            reversed_column[index] = "X" if player == 1 else "O"
            break
    if index == "":
        return False
    column = reversed_column[::-1]
    fields[num] = column
    draw_board(fields)
    return True


def checkIfFourInRow():
    winner = False
    for column in fields:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i - 1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                winner = column[i - 1]
                return winner
    return winner


def checkIfFourInColumn(column_matrix):
    winner = False
    for column in column_matrix:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i - 1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                winner = column[i - 1]
                return winner
    return winner


def checkIfFourInForwardDiagonal(column_matrix, player):
    for i in range(0, len(column_matrix)):
        for j in range(0, len(column_matrix[i])):
            try:
                if column_matrix[i][j] == player and column_matrix[i + 1][j - 1] == player and column_matrix[i + 2][
                    j - 2] == player and column_matrix[i + 3][j - 3] == player:
                    return True
            except IndexError:
                next

    return False


def checkIfFourInBackwardDiagonal(column_matrix, player):
    for i in range(0, len(column_matrix)):
        for j in range(0, len(column_matrix[i])):
            try:
                if column_matrix[i][j] == player and column_matrix[i + 1][j + 1] == player and column_matrix[i + 2][
                    j + 2] == player and column_matrix[i + 3][j + 3] == player:
                    return True
            except IndexError:
                next
    return False


def isValidMove(column_no):
    if column_no >= 1 and column_no <= 7:
        return True
    else:
        return False


def createColumnMatrix():
    column_matrix = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " "]]
    # for limit of player, player term is only onder 7
    for i in range(7):
        for j in range(len(fields[i])):
            column_matrix[j][i] = fields[i][j]

    return column_matrix


def startConnect4():
    player = 1
    no_win = True
    winner = ""
    while (no_win):
        ask_column = colored('Player ' + str(player) + ' turn, enter the column number:\n', "yellow", attrs=["bold"])
        column_no = input(ask_column)
        if column_no:
            column_no = int(column_no)
            if isValidMove(column_no) == False:
                cprint('Hey, YOUR MOVE IS GONE WRONG...... Try again.\n', 'red', attrs=['bold'])
            else:
                updated_flag = updateBoard(column_no - 1, player)
                if updated_flag:
                    print("")
                    current_player = player
                    tile = "X" if player == 1 else "O"
                    player = 2 if player == 1 else 1
                    winner = checkIfFourInRow()
                    if winner:
                        no_win = False
                    else:
                        column_matrix = createColumnMatrix()
                        winner = checkIfFourInColumn(column_matrix)
                        if winner:
                            no_win = False
                        elif checkIfFourInBackwardDiagonal(column_matrix, tile):
                            winner = current_player
                            no_win = False
                        elif checkIfFourInForwardDiagonal(column_matrix, tile):
                            winner = current_player
                            no_win = False
                else:
                    cprint('Hey, this is not a right move. Try again.\n', 'red', attrs=['bold'])
        else:
            cprint('Hey, this is not a right move. Try again.\n', 'red', attrs=['bold'])

    if winner == "X":
        winner = "1"
    else:
        winner = "2"
    cprint('congratulation, YEH.......YOU ARE THE WINNER ' + str(winner), 'blue', attrs=['bold'])


print('Starting Connect 4 Game... Get ready!\n')

draw_board(fields)
startConnect4()