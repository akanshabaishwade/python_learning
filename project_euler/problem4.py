# n = 0
# for a in range(999, 100, -1):
#     for b in range(a, 100, -1):
#         x = a * b
#         if x > n:
#             s = str(a * b)
#             # ?
#             if s == s[::-1]:
#                 n = a * b
# print(n)
c = 0
def paindrome_number(a):

    for i in a :
        t = i
        rev = 0
        while t > 0:
            rev = rev*10 + t % 10
            t = t // 10
        if rev == i:
            print(i)
            c = c +1

print()
print("total paindrome number are:", c)
print()
def main():
    a =[10, 121, 133, 155, 141, 252]
    paindrome_number(a)

if __name__=="__main__":
    main()