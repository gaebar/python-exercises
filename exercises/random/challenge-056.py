### RANDOM CHALLENGE ###

"""
056
Randomly pick a whole number between 1 and 10. 
Ask the user to enter a number and keep entering numbers 
until they enter the number that was randomly picked.
"""

# I have added a function that is reused across exercises
import common_functions
import random

computer_choice = random.randint(1, 10)

# to avoid the break statement, I have encapsulated the logic into a function


def ask_for_user_choice(computer_choice, user_choice):
    correct = False
    while correct == False:
        user_choice = common_functions.get_user_input(
            "Pick a number between 1 and 10: ")
        if user_choice == computer_choice:
            correct == True
            print(f"Correct! Computer choice was {computer_choice}")
            return


def challenge_056(computer_choice):
    user_choice = common_functions.get_user_input(
        "Pick a number between 1 and 10: ")
    ask_for_user_choice(computer_choice, user_choice)


challenge_056(computer_choice)
