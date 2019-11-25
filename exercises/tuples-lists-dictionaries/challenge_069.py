# TUPLES, LISTS AND DICTIONARIES

# Challenge 069
"""
Create a tuple containing the names of five countries and display the whole tuple.
Ask the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple.
"""

country_names = (
    "England",
    "Italy",
    "Spain",
    "France",
    "Portugal"
)

print(country_names)


# Ask for user input and ensuring the user entering an integer
def get_user_input(message):
    while(True):
        user_input = input(message)
        if user_input.isnumeric():
            print("Please enter a country name:")
        elif len(user_input) <= 2:
            print("Please enter at least three caracters.")
        else:
            return user_input


def ask_for_user_choice():
    while(True):
        user_choice = get_user_input(
            "Please enter one of the countries above: ")
        if user_choice not in country_names:
            print("This country is not in the list, please try again:")
        else:
            return user_choice


def print_msg(user_choice, country_name):
    print(f"{user_choice} has index number {country_names.index(user_choice)}")


def main():
    user_choice = ask_for_user_choice()
    print_msg(user_choice, user_choice)


main()
