### RANDOM CHALLENGE ###

"""
057
Update program 056 so that it tells the user
if they are too high or low before they pick again.
"""

# Play around to understand more: added a different message if user guess doesn't match.
import random

computer_choice = random.randint(1, 10)
correct = False


def check_user_choice():

    while correct == False:
        user_choice = int(input("Pick a number between 1 and 10: "))
        if user_choice == computer_choice:
            correct == True
            print("You rock! Computer choice matched.", int(computer_choice))
            return
        elif user_choice > computer_choice:
            print("Too high")
        else:
            print("Too low")


check_user_choice()
