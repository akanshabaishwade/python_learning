#
# while condition:
#       action
#         action
# foo = 6
#
# while foo > 3:
#     foo = 100
#
#     print("oh it was good")
#     print(foo)
# counter = 5
# while 31 > 30:
#     # print((counter + 30), "1st print")
#     counter = counter + 100
#     print(counter)
# print(counter)
# var1 = 5
# var2 = 0
# while var1 < 100:
#     print(var1)
#     var1 = var1 + 1
#     print(var1, "it is 1st var1 after adding one")
#     var2 = var2 + var1
#     print(var2, "it is current var2")
#     var1 = var1 + 1
#     print(var1, "here add one")
#     print(var2, "it is var2")
#     print("=========")
# # print(var2)
# x = 'abcd'
# for i in range(len(x)):
#     print(i)
#     print(x)
# Letter = ["c", "a", "b", "c", "a", "b", "c""a", "b", "c","a", "b", "c"]
# Index = 0
# while Index < len(Letter):
#     print("letter index is grater then Index")
#     print(Index)
#     print(Letter[Index])
#     Index += 1
# print(Letter.count("a"), "number of a")
height = 2000
velocity = 0.1
time = 0
while height > 0:
    height = height - velocity
    print(height, "it is current hight")
    print("======")
    velocity += 1
    print(velocity)
    time = time + 1
    print(time, "it is a time")
print(height)
print(velocity)
print(time, "it is a time")














