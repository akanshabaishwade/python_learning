ParticipantNumber = 2
participlantData = []
registeredparticipants = 0
# use while loop and if registeredparticipants is less than ParticipantNumber
while(registeredparticipants < ParticipantNumber):
    # create empty list for put some data

    # create variable, user input for name
    name = input("please enter your name: ")
    # create variable, user inout for country
    country = input("please enter your country of origin: ")
    age = int(input("please enter your age: "))
    tempartData = {"name": name,
                   "country": country,
                   "age": age}
    participlantData.append(tempartData) #[tempartdata]
    # add one in every loop
    registeredparticipants += 1

for participant in participlantData:
    print(f"name is {participant['name']}")
    print(f"age is {participant['age']}")
    print(f"country is {participant['country']}")