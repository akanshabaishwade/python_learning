def main():
    a = set("we are gonna a biggest boat.")
    b = set("i am sorry, Dave. I am afraid i can't do that")
    print_set(a)
    print_set(sorted(b))
    print_set(a | b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end='')
    print('}')
main()
