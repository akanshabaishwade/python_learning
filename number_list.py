import typing
import numpy as np


def number_list(a: typing.List):
    #  print(f"Min = {min(a)}")
    # print(f"Max = {max(a)}")
    sum_of_list = 0
    count = 0
    greatest = 0
    smallest = a[0]
    for i in a:
        sum_of_list = sum_of_list + i
        count = count + 1
        if i > greatest:
            greatest = i
        if smallest > i:
            smallest = i
    sorted_alist = sorted(a)
    second_smallest = sorted_alist[1]
    # print(type(second_smallest))
    # print(second_smallest[1])
    second_greatest = sorted_alist[-2]
    print("Average = {}".format(sum_of_list/count))
    print("NP Average = {}".format(np.mean(a)))
    print(f"Greatest = {greatest}")
    print("Greatest ={abc}, Smallest = {efg}".format(efg=smallest, abc=greatest))
    print("Second Smallest element = {}".format(second_smallest))
    print(sorted_alist)
    print("second_greatest= {}".format(second_greatest))


number_list([3, 5, 7, 89, 54, 78, 12])
print("======")
number_list([89, 94, 78, 90, 34, 3])
