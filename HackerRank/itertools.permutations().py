from itertools import permutations

word, num = input().split(" ")
permut = list(permutations(word, int(num)))
permut.sort()

[print("".join(i)) for i in permutations]
