"""
Define a subprogram that will ask the user to pick a low and a high number,
and then generate a random number between those two values and store it in
a variable called “comp_num”.

Define another subprogram that will give the instruction “I am thinking
of a number…” and then ask the user to guess the number they are thinking of.

Define a third subprogram that will check to see if the comp_num is the same
as the user’s guess. If it is, it should display the message “Correct, you
win”, otherwise it should keep looping, telling the user if they are too low or
too high and asking them to guess again until they guess correctly.
"""

import random
import common_functions


def ask_for_user_numbers():
    num_low = 0
    num_high = 0

    while num_low >= num_high:
        num_low = common_functions.get_user_input_integer(
            "Please, enter the minimum number: "
        )
        num_high = common_functions.get_user_input_integer(
            "Please, enter the maximum number: "
        )

        print(
            "Please ensure that the minimum number is smaller than the maximum number"
        )

    return random.randrange(num_low, num_high)


def prompt_for_guess():
    print("\nI am thinking of a number… ")
    guess = common_functions.get_user_input_integer(
        "Please, enter the number I am thinking of: "
    )
    return guess


def check_user_choice(computer_choice, user_guess):
    while True:
        if computer_choice == user_guess:
            print("Correct, you win!")
            return

        if user_guess > computer_choice:
            user_guess = common_functions.get_user_input_integer(
                "Please, enter a lower number: "
            )
        else:
            user_guess = common_functions.get_user_input_integer(
                "Please, enter a higher number: "
            )


def challenge_119():
    computer_choice = ask_for_user_numbers()
    user_guess = prompt_for_guess()
    check_user_choice(computer_choice, user_guess)


if __name__ == "__main__":
    challenge_119()
