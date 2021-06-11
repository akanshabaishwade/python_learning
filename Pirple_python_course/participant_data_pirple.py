ParticipantNumber = 2
participlantData = []
registeredparticipants = 0
outputfile = open("participant.txt", "w")
# use while loop and if registeredparticipants is less than ParticipantNumber
while(registeredparticipants < ParticipantNumber):
    # create empty list for put some data
    tempartData = []
    # create variable, user input for name
    name = input("please enter your name: ")
    # put all data (append) from name in empty list (tempartdata)
    tempartData.append(name)
    # create variable, user inout for country
    country = input("please enter your country of origin: ")
    # also append country data from tempartdata
    tempartData.append(country)
    # print tempartData  for all append data
    print(tempartData)
    # create variable with user input and add age
    age = int(input("please enter your age: "))
    # append age also
    tempartData.append(age) # [name, country, age]
    # use append for all list show and add in output
    participlantData.append(tempartData) #[tempartdata]
    print(participlantData)
    # add one in every loop
    registeredparticipants += 1

for participlant in participlantData:
    for data in participlant:
        outputfile.write(str(data))
        outputfile.write(" ")
    outputfile.write("\n")
outputfile.close()

inputfile = open("participant.txt", "r")
inputlist = []

for line in inputfile:
    tempparticipal = line.strip().split()
    # print(tempparticipal)
    inputlist.append(tempparticipal)
#     "max u.s. 21 \n".strip("\n") -> "max u.s. 21"
#      "max u.s 21.spit() ["max", "u.s"]


Age = {}
for temage in inputlist:
    if temage[-1] in Age:
        Age[temage[-1]] += 1

    else:
        Age[temage[-1]] = 1

print(Age)
Oldest = 0
youngest = 100
mostOccringage = 0
counter = 0
for temage in Age:
    if temage > Oldest:
        Oldest = temage
    if temage < youngest:
        youngest = temage
print(Oldest)
print(youngest)
print("most accuring age is:", mostOccringage, "with", counter, "participents")

inputfile.close()





















