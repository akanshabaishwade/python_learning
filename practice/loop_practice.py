def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                # print(num, "is not a prime number")
                # print(i, "times", num // i, "is", num)
                # break
                return False
        else:
            return True

    else:
        return False

for number in range(101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif is_prime(number):
        print("Prime")
    else:
        print(number)

