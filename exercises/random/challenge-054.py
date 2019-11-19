### RANDOM CHALLENGE ###

"""
054
Randomly choose either heads or tails ("h" or "t"). Ask the user to make their choice. 
If their choice is the same as the randomly select value, display the message "You Win",
otherwise display "Bad luck".
At the end, tell the user if the computer selected heads on tails.
"""

import random
computer_choice = random.choice(["h", "t"])
user_choice = input("For this game, choose heads or tails ('h'/'t'): ")
if user_choice == computer_choice:
    print("You Win!")
else:
    print("Bad luck!")
if computer_choice == "h":
    print("Computer choice was head!")
else:
    print("Computer choice was tail!")
