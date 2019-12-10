# TUPLES, LISTS AND DICTIONARIES

# Challenge 074
"""
Enter a list of ten colours. Ask the user for a starting number between 0 and 4 
and an end number between 5 and 9. Display the list for those colours between 
the start and end numbers the user input.
"""

# note: check for Python local input
from exercises.tuples_lists_dictionaries import common_functions

colours = [
    "red",
    "blue",
    "white",
    "yellow",
    "green",
    "grey",
    "purple",
    "black",
    "brown",
    "pink",
]


def get_check_input(start, end):
    outside_range_message = "The number is outside the given range. Try again"
    starting_number_message = f"Enter a starting number ({start}-{end}): "

    value = common_functions.get_user_input_integer(starting_number_message)

    while value not in range(start, end + 1):
        print(outside_range_message)
        value = common_functions.get_user_input_integer(starting_number_message)
    return value


def ask_for_user_input():
    start = get_check_input(0, 4)
    end = get_check_input(5, 9)

    return (start, end)


def challenge_74(colours):
    (start, end) = ask_for_user_input()
    trimmed_colours = colours[start:end]
    print(", ".join(trimmed_colours))


if __name__ == "__main__":
    challenge_74(colours)
