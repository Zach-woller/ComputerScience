import random

random_number = random.randint(1, 101)

guesses = 0

guess = ""
try:  
    guess = input("Guess a number between 1 and 100\n>")
except: 
    print("hmm")

while random_number != guess:
    guess = + 1
    guess = int(input("Guess a number between 1 and 100\n>"))
    guess = int(guess)
    if guess < random_number:
        print("higher")
    elif guess > random_number:
        print("lower")
    else: 
        print("Good job it was" + str(random_number))

