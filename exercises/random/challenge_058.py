### RANDOM CHALLENGE ###

"""
058
Make a maths quiz that asks five questions by randomly generating two whole number 
to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer.
If they get it right add a point to the score. At the end of the quiz, 
tell them how many they got correct out of five.  
"""

import random
import operator

# using dictionary to take random operators


def randomCalc():
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv}
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1, num2)
    print(f'What is {num1} {op} {num2}?')
    return answer


def ask_for_user_choice():
    answer = randomCalc()
    guess = float(input())
    return guess == answer


def quiz():
    print('Welcome! This is a 5 question math quiz')
    score = 0
    for i in range(5):
        correct = ask_for_user_choice()
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!\n')
    print(f'You scored {score} out of 5')


quiz()
