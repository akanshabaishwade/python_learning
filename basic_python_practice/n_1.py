# create function name bord with two argument
def bord(n, m):
    # for loop for column range 1 to n+1
    for row in range(1, n + 1):

        # print(row)
        # for loop for column
        for column in range(1, m + 1):
            # create new variable for run new loop for square of row that's why var = row
            var = row
            # new for loop range column because we want square of column
            for mult in range(column):
                # for remove 1st that is equal to 0
                if mult != 0:

                    var = var * row

            print(var, end=" ")
        print("")


bord(9, 5)
