print('Welcome to the Quiz Game')

# Does user wants to play the quiz game? 
playing = input("Continue? : ")
if playing.lower() != 'yes':
    quit()
print('Okey, let\'s play :)')
score = 0
# Function for asking the question and checking the answer
def game_logic(question, ans):
    global score
    print(question)
    answer = input('> ')
    # Converting user input into lowercase
    if answer.lower() == ans:
        print('Correct!')
        score += 1
    else:
        print("That's a wrong answer")

# Supplying questions and answers
game_logic('What does CPU stands for?', 'central processing unit')
game_logic('What does GPU stands for?', 'graphics processing unit')
game_logic('What does PSU stands for?', 'power supply unit')
print('')

# Displaying the score in percentage
print('Your Score: ' + str(int((score / 3) * 100)) + '%')
