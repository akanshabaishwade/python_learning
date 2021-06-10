# element = {'boy', 'joo', 'aditi', 'sidhdhi', 'babu', 'babu'}
# # why this siris is not same
#
# print(set(element))
# if "b" in element:
#     print("oh it was nice")
# print(element)
# class_toppers = []
# for i in range(1, 5):
#     student =input(f"who is {i}st in class - ")
#     class_toppers.append(student)
# main_list = set(class_toppers)
# print(main_list)
# print(class_toppers)
# class_toppers = []
# class_list = []
# for count in range(1, 4):
#     student =input(f"who is {count}st in class - ")
#     class_toppers.append(count)
#     class_list.append(student)
# main_list = set(class_toppers)
# # print(main_list)
# print(class_toppers)
# print(class_list)
# ====================================================
# empty list
family_member = []
# empty dictionary
member_name = {}
# for loop use in range 1 to 5 start 1 and not included 5
for time in range(1, 5):
      # create new variable(member) and use input function and write inner bracket massage and use{} for "forloop" variable
    member =input(f'who is eat 1 roti in  {time} pm if you,Enter your name - ')
    # append list(family_member) to inner loop variable(member) for fill the list(family_member)
    family_member.append(member)
    # use if for dictionary we fill the loop(member) in dict(member_name)
    if member in member_name:
    #     here we chack if membe's element in already in member_name it mean dictionry so add +1 if not go to else
        member_name[member] += 1
    #     if member's is not in dictionary  so in this case equal to 1
    else:

        member_name[member] = 1
#         print member name
print(member_name)


