# make two variable for starting 1 and 2 number
first_num, Secound_num = 0, 24
# create blank list for append result
series_list = []
# create limit
max_series = 5000
# use for loop using range secound num to max limit
for value in range(Secound_num, max_series):
    # use if statement
    if value % 8 == 0 and value % 12 == 0:
        # here we are doing f + s
        nth = first_num + Secound_num
        #  f == s and s == nth, nth is a new number every loop use new number as first number
        first_num = Secound_num
        Secound_num = nth
        # if nth is bigger then max so, breck the loop
        if nth >= max_series:
            break
        #     append and square "nth" in series_list
        series_list.append(nth*nth)

# call def fiction
print(series_list)



