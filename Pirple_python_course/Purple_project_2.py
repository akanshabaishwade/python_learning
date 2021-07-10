import random

name = input("What is your name? ")

print("Wel come.... ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:
    failed = 0

    for char in word:

        if char in guesses:
            print(char)

        else:
            print("_")

            failed += 1

    if failed == 0:

        print("You Win")
        print("The word is: ", word)
        break

    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")

        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
