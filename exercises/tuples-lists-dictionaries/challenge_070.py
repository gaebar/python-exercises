# TUPLES, LISTS AND DICTIONARIES

# Challenge 070
"""
70: Add to program 069 to ask the user a number and display the country in that position.
"""

country_names = ("England", "Italy", "Spain", "France", "Portugal")

print(country_names)


# Ask for user input and ensures the user enters an integer
def get_user_input_digit(message):
    while True:
        user_input = input(message)
        if not user_input.isdigit():
            print("Oops! That was not a valid number. Try again...")
        else:
            return int(user_input)


def ask_for_country_by_index():
    while True:
        user_index_choice = get_user_input_digit("Enter a number between 0 and 4: ")
        if user_index_choice >= len(country_names) - 1:
            print("This number is too high")
        else:
            return (user_index_choice, country_names[user_index_choice])


def print_msg(user_index, user_country):
    print(f"The country with index {user_index} is {user_country}.")


def main():
    (user_index, user_country) = ask_for_country_by_index()
    print_msg(user_index, user_country)


main()
