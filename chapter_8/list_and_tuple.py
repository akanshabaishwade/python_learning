def main():
    game = ['Rock', 'paper', 'scissors', 'lizard', 'spock']
    print(game[1:5:2])
    print_list(game)

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
        print()

if __name__ == '__main__':
    main()