song_game = {"song name": "Roli me ghumi ghumi", "singer": "honey singh", "composer": "honey singh", "release_date": "16-02-2000", "theme":"rap song"}

# create function name ask_keys
def ask_keys():
    # create two variable one is key and second is value and use input function in them for OUTPUT display key and value
    key = input("\nGreat, let\'s start the game, guess the key? - \n")
    value = input("\nWhat you think is the value of " + key + "?\n")
    # here we use if statement if key and current key is equal in both are small letter  and check if condition

    if key and value:
        key = key.lower()
        value = value.lower()

        if key in song_game and song_game[key].lower() == value:
            return True
    return False


def Game():
    if ask_keys():
        print("You guessed it right...")
    else:
        print("Oh... you are wrong")
        repeat = input("\nWanna play again? Say 'yes' to continue or say 'no'.\n")
        if repeat.lower() == "yes":
            Game()
        else:
            print("\nSee you again!")




print("Starting game....")

Game()