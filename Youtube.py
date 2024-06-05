import random

sn = random.randint(1, 15)

print("This is a guessing game, please give me a number between 1 and 15")

g = int(input("please give me your number"))

while g != sn:
    if g < sn:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    g = int(input("please give me your number"))

print("That's right")