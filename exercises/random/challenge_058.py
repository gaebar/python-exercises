### RANDOM CHALLENGE ###

"""
058
Make a maths quiz that asks five questions by randomly generating two whole number 
to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer.
If they get it right add a point to the score. At the end of the quiz, 
tell them how many they got correct out of five.  
"""
import common_functions

import random
import operator

# using dictionary to take random operators


def random_calc(current_index, total_questions):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    chosen_operator = random.choice(list(operations.keys()))
    answer = operations.get(chosen_operator)(num1, num2)
    message = f"Question {current_index} of {total_questions} - What is {num1} {chosen_operator} {num2}? "
    return (answer, message)


def ask_for_user_choice(current_index, total_questions):
    (answer, message) = random_calc(current_index, total_questions)
    guess = common_functions.get_user_input_float(message)
    return guess == answer


def quiz():
    print("Welcome! This is a 5 questions math quiz")
    score = 0
    total_questions = 5
    for i in range(total_questions):
        correct = ask_for_user_choice(i + 1, total_questions)
        if correct:
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect!\n")
    print(f"You scored {score} out of 5")


quiz()
