import  random
suits = ["Hearts", "Spends", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "King", "Queen", "Card- A"]
Toss = []
for suit in suits:
    for rank in ranks:
        Toss.append(f'{rank} of {suit}')
    print(f'There are {len(Toss)} cards in Toss.')
    print("start Game.....")

    player1 = []
    player2 = []
    while len(player1) < 5:
        card = random.choice(Toss)
        Toss.remove(card)
        player1.append(card)
        card2 = random.choice(Toss)
        Toss.remove(card2)
        player2.append(card2)
    # print(f'There are {len(Toss)} cards in Toss.')
    print('Player1 has the following cards in their hand: ')
    print(player1)
    print('player2 has the following cards in their hand: ')
    print(player2)