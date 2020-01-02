# MORE STRING MANIPULATION

# Challenge 080
"""
Ask the user to enter their first name and then display the length of their first name.
Then ask for their surname and display the length of their username. Join their first name
and surname together with a space between and display the result.
Finally, display the length of their full name (including the space).
"""


def processing(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name


def length_of(user_input):
    return len(user_input)


def display_length_name():
    user_first_name = input("Please, enter your name: ")
    user_first_name_length = length_of(user_first_name)
    print(f"Your name has {user_first_name_length} characters in it.")

    user_last_name = input("Enter your last name: ")
    user_last_name_length = length_of(user_last_name)
    print(f"Your surname has {user_last_name_length} characters in it.")

    full_name = processing(user_first_name, user_last_name)
    user_full_name_length = length_of(full_name)
    print(
        f"Your full name is {full_name} and has {user_full_name_length} characters in it."
    )


if __name__ == "__main__":
    display_length_name()
