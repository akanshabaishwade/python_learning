ParticipantNumber = 2
participlantData = []
registeredparticipants = 0
outputfile =open("participant_data_data.txt", "w")
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
for participant in participlantData:
    for data in participant:
        outputfile.write("\n")
outputfile.close()
inputfile = open ("participant_data_copy.txt", "r")
inputlist = []

for line in inputfile:
    tempParticipant = line.strip("\n").split()

inputfile.close()