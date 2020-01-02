"""
Define a subprogram that will ask the user to pick a low and a high number, 
and then generate a random number between those two values and store it in  
a variable called  “comp_num”. 

Define another  subprogram that will  give the instruction 
“I am  thinking of a number…” and then ask the user to guess the number they are thinking of.  

Define a third subprogram that will check to see if the comp_num is the same as the user’s guess. 
If it is, it should display the message “Correct, you win”, otherwise it should keep looping, 
telling the user if they are too low or too high and asking them to guess again until they  
guess correctly. 
"""

import random


def user_pick():
    num_low = int(input("Please, enter a low number: "))
    num_high = int(input("Please, enter a high number: "))
    comp_num = random.randrange(num_low, num_high)
    return comp_num


def given_instructions():
    print("\nI am thinking of a number… ")
    guess = int(input("Please, enter the number I'm thinking of: "))
    return guess


def check_user_choice(comp_num, guess):
    try_again = True
    while try_again == True:
        if comp_num == guess:
            print("Correct, you win")
            try_again = False
        elif comp_num > guess:
            guess = int(input("Please, enter a low number: "))
        else:
            guess = int(input("Please, enter a high number: "))


def challenge_119():
    comp_num = user_pick()
    guess = given_instructions()
    check_user_choice(comp_num, guess)


if __name__ == "__main__":
    challenge_119()
