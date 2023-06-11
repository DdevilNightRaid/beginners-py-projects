uname = input("Enter your username: ")
print(f"Welcome, {uname} to this adventure..!")
print("")
print("You are traveling alone in a pathway in the middle of the forest, You came across two path one leading left and another leading right.")
answer = input("Which one do you want to pick? [left or right]: ")

if answer.lower() == 'left':
    # some code
    q0 = input("A river shows up do you want to cross it by swimming or do you want to walk accross? [swim, walk]")
    if q0.lower() == 'swim':
        print("You were taken down by crocs.")
    elif q0.lower() == 'walk':
        print("You came across a lion")
        q2 = input("Do you want to get climb the tree or run away? [climb, run]: ")
        if q2.lower == 'climb':
            print("You died, lion attacked you while climbing.")
        else:
            print("Lion sensed you and attacked you.")
    else:
        print("You lose.")
elif answer.lower() == 'right':
    #some code
    print("You fell from a cliff.")
else:
    print("You lose")