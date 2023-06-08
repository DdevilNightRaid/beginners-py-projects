import random
random_number = random.randint(0, 101)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print("You guess it right..!")
            break
        elif user_guess > random_number:
            print("Your guess was higher")
            continue
        else:
            print("Your guess was lower")
            continue
    else:
        print("Please type a number next time..!")
        continue
print("You took " + str(guesses) + " guesses")