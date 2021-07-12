import collections


num_of_shoes = int(input())
shop = collections.Counter(map(int, input().split()))

total_cost = 0

for i in range(int(input())):
    size, price = map(int, input().split())
    if shop[size]:
        total_cost += price
        shop[size] -= 1

print(total_cost)