variable = input("message to the user")
Name = input("Enter your name: ")
print(Name)
scores = []
for i in range(5):
    curretscores = float(input("please enter the score"))
    scores.append(curretscores)
    print("the score you entered was: \n")
print(scores)