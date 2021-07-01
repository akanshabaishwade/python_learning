from random import randint

randVal = int(randint(0, 100))
while (True):
    guess = input("please enter your guess: ")
    if guess == randVal:
        break
    elif guess < randVal:
        print("Your guess was too low")
    else:
        print("too high")
print("you guessed correctly with: ", guess)


