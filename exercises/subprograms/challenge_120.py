"""
Display the following menu to the user:  1) Addition, 2) Subtraction and Enter
1 or 2. If the user enters 1, it should run a subprogram that will generate two
random numbers between 5 and 20, and ask the user to add them together. Work
out the correct answer and return both the user’s answer and the correct answer.

If they entered 2 as their selection on the menu, it  should run a subprogram
that will generate one number between 25 and 50 and another number between 1
and  25 and ask them to work out num1 minus num2. This way they will not have
to worry about negative answers. Return both the user’s answer and the correct
answer.

Create another subprogram that will check if the user’s answer matches
the actual answer. If it does, display  “Correct”, otherwise display a message
that will say “Incorrect, the answer is” and display the real answer. If they
do not select a relevant option on the first menu  you should display a
suitable message.
"""

import random
import operator

OPERATIONS = {"+": operator.add, "-": operator.sub}


def get_user_input_integer(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        print("Oops! That was not a valid number. Try again...")


def ask_for_user_input():
    return get_user_input_integer("Your answer: ")


def check_answer(num_1, num_2, operation, user_answer):
    correct_answer = OPERATIONS.get(operation)(num_1, num_2)
    return (user_answer == correct_answer, correct_answer)


def display_response(is_answer_correct, correct_answer):
    if is_answer_correct:
        print("Correct!")
    else:
        print(f"Incorrect, the answer was {correct_answer}")


def process(min1, max1, min2, max2, operation):
    num_1 = random.randint(min1, max1)
    num_2 = random.randint(min2, max2)
    print(f"{num_1} {operation} {num_2} =")
    user_answer = ask_for_user_input()
    return check_answer(num_1, num_2, operation, user_answer)


def challenge_execution():
    print("1) Addition \n2) Subtraction")

    user_input = get_user_input_integer("Enter 1 or 2: ")

    if user_input == 1:
        (is_answer_correct, correct_answer) = process(5, 20, 5, 20, "+")
    elif user_input == 2:
        (is_answer_correct, correct_answer) = process(25, 50, 1, 25, "-")
    else:
        print("Incorrect selection")
        return

    display_response(is_answer_correct, correct_answer)


if __name__ == "__main__":
    challenge_execution()
