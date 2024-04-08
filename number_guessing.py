import random
import math

'''
number guessing game
'''

# ------------ Version 1 --------------------------------------
'''lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_number = random.randint(lower_bound, upper_bound)
print("Random", random_number)

guess = int(input("Enter your guess: "))
count = 1

while guess != random_number:
    if guess < random_number:

        if count <= 5:
            print("Too low,Try again")
            guess = int(input("Enter your guess: "))
            count += 1
            print("count: ",count)
        else:
            break
    else:
        if count <= 5:
            print("Too high,Try again")
            guess = int(input("Enter your guess: "))
            count += 1
            print("count: ",count)
        else:
            break
print("Congratulations, You fixed it!")'''

# ------------------ Version 2--------------------------------

'''
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_number = random.randint(lower_bound, upper_bound)

count = 0

while count <= 10:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess == random_number:
        print("Congratulations, you fixed it!, in ",count," trials")
        break

    elif guess < random_number:
        print("Too low,try again")
    elif guess > random_number:
        print("Too high,try again")
'''


# -------------------------version 3 ---------------------------------------------

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_number = random.randint(lower_bound, upper_bound)

trials = round(math.log(upper_bound-(lower_bound+1),2),0)


print("\tYou have ",trials,"trials to get the number")

count = 0
while count < trials:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess == random_number:
        print("Congratulations, you fixed in",count," trials")
        break

    elif guess < random_number:
        print("Too low,try again")
        print("You have ",trials-count,"trials remaining")
        print()
    elif guess > random_number:
        print("Too high,try again")
        print("You have ", trials - count, "trials remaining")
        print()

if count >= trials:
        print("The Number was:-",random_number, "Best of Luck Next time")
