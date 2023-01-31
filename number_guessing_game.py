import random

print("Wellcome to number guessing game!")
random_num = random.randrange(-10, 11)
guess_counter = 0
while True:
    guess_counter += 1
    guess2 = input("Try to guess the number: ")
    if guess2.lstrip("-").isdigit():
        guess2 = int(guess2)
        if guess2 > 11:
            print("Please enter a number smaller than 11 next time.")
            quit()
        if guess2 < -10:
            print("Enter a number bigger than -10.")
        elif guess2 > random_num:
            print("You are above it.")
        elif guess2 < random_num:
            print("You were below it.")
        else:
            print("You got it! :)")
            print("You did it in", guess_counter, "tries.")
            quit()
    else:
        print("Enter a number next time.")
        quit()
