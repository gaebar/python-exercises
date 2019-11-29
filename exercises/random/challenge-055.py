### RANDOM CHALLENGE ###

"""
055
Randomly choose a number between 1 and 5. Ask the user to pick a number. 
If they guess correctly, display the message "Well done!", otherwise tell them 
if they are too high or too low and ask them to pick a second number. 
If they guess correctly on their second guess, display "Correct",
otherwise dispaly "You lose".
"""

""" Added a expect ValueError"""

import random
import common_functions

random_number = random.randint(1, 5)


def check_correct_answer(random_number, user_number):
    if random_number == user_number:
        print("Correct!")
    else:
        print("Sorry, you lose.")


def check_answer(message, random_number, user_number):
    user_number = common_functions.get_user_input(message)
    check_correct_answer(random_number, user_number)


def challenge_055():
    user_number = common_functions.get_user_input("Pick a number between 1 and 5: ")
    if random_number == user_number:
        print("Well done!")
    elif random_number < user_number:
        check_answer("Too high! Pick another number: ", random_number, user_number)
    elif random_number > user_number:
        check_answer("Too low! Pick another number: ", random_number, user_number)

    # Display computer choice
    print(f"Computer choice was {random_number}")


challenge_055()
