import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']
while True:
    user_input = input("Type R / P / S or Q: ").lower()
    if user_input == 'q':
        break

    if user_input not in ['r', 'p', 's']:
        continue
    
    #Get computer's choice
    random_number = random.randint(0, 2)
    computer_choice = options[random_number]

    print("Computer Picked: " + computer_choice)

    if user_input == 'r' and computer_choice == 'scissors':
        print("You won")
        user_wins += 1
    elif user_input == 'r' and computer_choice == 'paper':
        print("You lost")
        computer_wins += 1
    elif user_input == 'r' and computer_choice == 'rock':
        print("It's a draw")
    elif user_input == 'p' and computer_choice == 'paper':
        print("It's a draw")
    elif user_input == 'p' and computer_choice == 'rock':
        print("You won")
        user_wins += 1
    elif user_input == 'p' and computer_choice == 'scissors':
        print("You lost")
        computer_wins += 1
    elif user_input == 's' and computer_choice == 'scissors':
        print("It's a draw")
    elif user_input == 's' and computer_choice == 'paper':
        print("You won")
        user_wins += 1
    else:
        print("You lost")
        computer_wins += 1

print("Bye :(")