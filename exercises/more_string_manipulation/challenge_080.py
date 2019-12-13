# MORE STRING MANIPULATION

# Challenge 080
"""
Ask the user to enter their first name and then display the length of their first name.
Then ask for their surname and display the length of their username. Join their first name
and surname together with a space between and display the result.
Finally, display the length of their full name (including the space).
"""


def processing(first_name, last_name):
    # full_name = first_name + " " + last_name
    full_name = f"{first_name} {last_name}"

    length_first_name = len(first_name)
    length_surname = len(last_name)
    length_full_name = len(full_name)
    return length_first_name, length_surname, length_full_name, full_name


def display_length_name():
    # INPUT
    user_first_name = input("Please, enter your name: ")
    user_last_name = input("Enter your last name: ")

    # PROCESSING
    (
        length_user_first_name,
        length_user_last_name,
        length_full_name,
        full_name,
    ) = processing(user_first_name, user_last_name)

    # OUTPUT
    print(f"Your name has {length_user_first_name} characters in it.")
    print(f"Your surname has {length_user_last_name} characters in it.")
    print(f"Your full name is {full_name} and has {length_full_name} characters in it.")


if __name__ == "__main__":
    display_length_name()
