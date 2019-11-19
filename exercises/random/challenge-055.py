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

random_num = random.randint(1,5)

def check_correct_answer(random_num, user_num):
    if random_num == user_num:
        print("Correct!")
    else:
        print("Sorry, you lose.")

def check_answer(message, random_num, user_num):
    user_num = common_functions.get_user_input(message)
    check_correct_answer(random_num,user_num)

def challenge_055():
    user_num = common_functions.get_user_input("Pick a number between 1 and 5: ")
    if random_num == user_num:
        print ("Well done!")
    elif random_num < user_num:
        check_answer("Too high! Pick another number: ", random_num, user_num)
    elif random_num > user_num:
        check_answer("Too low! Pick another number: ", random_num, user_num)

    # Display computer choice
    print (f"Computer choice was {random_num}")

challenge_055()