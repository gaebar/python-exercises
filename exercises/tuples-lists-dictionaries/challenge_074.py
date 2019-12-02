# TUPLES, LISTS AND DICTIONARIES

# Challenge 074
"""
Enter a list of ten colours. Ask the user for a starting number between 0 and 4 
and an end number between 5 and 9. Display the list for those colours between 
the start and end numbers the user input.
"""


def get_user_input_integer(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        print(f"Oops! {user_input} is not a valid number. Try again...")


def get_check_input(
    start, end, message="The number is outside the given range. Try again"
):
    value = get_user_input_integer(f"Enter a starting number ({start}-{end}): ")
    while value not in range(start, end + 1):
        print(message)
        value = get_user_input_integer(f"Enter a starting number ({start}-{end}): ")
    return value


def ask_for_user_input():
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

    start = get_check_input(0, 4)
    end = get_check_input(5, 9)

    return colours[start:end]


def challenge_74():
    colours = ask_for_user_input()
    print(", ".join(colours))


challenge_74()
