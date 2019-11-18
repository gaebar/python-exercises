### RANDOM CHALLENGE ###

"""
056
Randomly pick a whole number between 1 and 10. 
Ask the user to enter a number and keep entering numbers 
until they enter the number that was randomly picked.
"""

# SOLUTION 1 
import random
computer_choice = random.randint(1, 10)
user_choice = int(input("Pick a number between 1 and 10: "))
while user_choice != computer_choice:
    print("Try again.")
    user_choice = int(input("Pick another number: "))
else:
    print("Correct! Computer choice was", int(computer_choice))


# SOLUTION 2 - please uncomment code to run it
# # Play around to understand more: modified the code to use the Boolean values

import random
computer_choice = random.randint(1, 10)
correct = False
while correct == False:
    user_choice = int(input("Pick a number between 1 and 10: "))
    if user_choice == computer_choice:
        correct == True
        print("Correct! Computer choice was", int(computer_choice))
        break
