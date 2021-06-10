vacation_spots = ["Ratanput", "bilaspur", "korba", "bhilai", "khamtarai"]
# vacation_file = open("vacation_places", "w")
# # here we use for loop for write file and add something
# for visit in vacation_spots:
#     # here give write command and add space (we can add any thing)
#     vacation_file.write(visit + " ")
# #     if open the file , so close command is importent for close file
# vacation_file.close()
# # here agian am commanted open vacation file use "r" for read
# vacation_file = open("vacation_places", "r")
# #
# first_line = vacation_file.readline()
# print(first_line)
# secoud_line = vacation_file.readline()
# print(secoud_line)
#
# finalsport = "madapur"
# vacation_file = open("vacation_places", "a")
# vacation_file.write(finalsport)
# vacation_file.close()
# vacation_file = open("vacation_places", "r")
# for line in vacation_file:
#     print(line, end="")
# vacation_file.close()
normal = open("../practice/vacation_spots", "a")
vacation_spots.append("anshu")
normal.close()
print(vacation_spots)



