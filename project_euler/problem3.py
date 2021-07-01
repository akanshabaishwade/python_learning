'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
# lower = 13000
# upper = 13195
# print("prinme number", lower, "to", upper, "are:")
# for num in range(lower, upper+1):
#     if num>1:
#         for i in range(2, num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)
# number choose krna jiska factor nikalna h
n = 600851475143
# i nam ka ek variable 2 even number sqr nikane k liye
i = 2
# use while loop i ka sqr root sath me n jo h wo bda hona chahiye srt se
while i * i < n:
    # yha pe devide krenge n ko i se, taki
    while n % i == 0:
        #
        n = n / i
    #     for find even number 2 + 1 = 3
    i = i + 1

print(int(n))

