secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5
while pw != secret:
    count += 1
    if count > max_attempt: break
    if count == 3:
        continue
    pw = input(f"{count}:what's the secret word?  ")
else:
    auth = True
print("Authorized" if auth else "calling the FBI....")

animals = ('bunny', 'loin', 'bear', 'dog', 'cat')
for pet in range(10):
    print(pet)
for pet in animals:
    if pet == 'dog':
        continue
    if pet == 'cat':
        break
    print(pet)
