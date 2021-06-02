name = "harry"
print(type(name))
print(name[0:4])
d = name [1:3:4]
name = input("Enter your name\n")
print("good morning, " + name)
letter = '''Dear <|NAME|>, 
hello congratulation you are selected 
wel come to our company
DATE: <|Date|>
'''
name = input("enter your name\n")
date = input("enter today's date")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)
st = "this is a sting with double spaces"
doubleSpaces = st.find("      ")

print(doubleSpaces)

