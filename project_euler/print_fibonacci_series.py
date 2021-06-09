nterms = int(100)


# first two terms
first_num, Secound_num = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print(nterms)
   print(first_num)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(first_num)
       nth = first_num + Secound_num

       first_num = Secound_num
       Secound_num = nth
       count += 1
       # i = d.append(nterms)
print(nterms)


