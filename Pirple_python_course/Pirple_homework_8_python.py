# inport os for read and write
import os
# create user input for variable file_name
file_name = input("Enter your File Name: ")
#  use if statement and add path give address with file name
if os.path.isfile("./" + file_name):
    # print and use format function format of file_name
    print("Looking for file {}".format(file_name))
    # print massage
    print("oh we found it....")
    # create variable it is user input and massage for user
    action = input(
        "What would you like to do with the file?\nPossible actions are: read, delete, append, replace\n")
    # here if statement if user say's read or choose read
    if action == "read":
        # print massage and....
        print("The content of the file:")
        # use with statement in upper line print with file_name
        with open(file_name, "r") as read_file:
            print(read_file.read())
    elif action == "append":
        text = input("Please enter your note: ")
        with open(file_name, "a") as append_file:
            append_file.write(text + "\n")
    elif action == "delete":
        os.remove("./" + file_name)
        print("{} have been deleted.".format(file_name))
        # I don't think it makes sense to create a new empty file right after deletion...
        # Anyway, this is the requested task so here it is
        with open(file_name, "w") as write_file:
            write_file.write("")
    #         use elif and command replace for replace it
    elif action == "replace":
        # create variable and make user input in int form
        line_num = int(
            input("Please enter the line number for the replacement: "))
        # make user input for user note
        text = input("Please enter your note: ")
        # use with for open the file for only read as new variable name read_file
        with open(file_name, "r") as read_file:
            # read_file in use read lines for space (one line one space)
            lines = read_file.readlines()
        #     do same thing for write file use with an as "w"
        with open(file_name, "w") as write_file:
            #
            for idx, line in enumerate(lines):
                # print(idx, line)
                if idx == line_num - 1:
                    print("Line num {} needs to be replaced!".format(line_num))
                    write_file.write(text + "\n")
                else:
                    print("Writing \"{}\"".format(line))
                    write_file.write(line)

    else:
        print("Sorry, unrecognized action")
else:
    print("Nope, this file does not exist, I'm going to create it for you!")
    text = input("Please enter your note: ")
    with open(file_name, "w") as write_file:
        write_file.write(text + "\n")