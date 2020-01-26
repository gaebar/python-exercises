"""
Create a program that will allow the user to easily manage a list of names.
You should display a menu that will allow them to add a name to the list,
change a name in the list, delete a name from the list or view all the names
in the list.
There should also be a menu option to allow the user to end the program.
If they select an option that is not relevant, then it should display a suitable
message. After they have made a selection to either add a name, change a name,
delete a name or view all the names, they should see the menu again without having
to restart the program. The program should be made as easy to use as possible.

"""
# used sys to terminate the progran execution
import sys


def get_user_input_integer(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        print("Oops! That was not a valid number. Try again...")


def get_user_input_string(message):
    while True:
        user_input = input(message)
        if user_input:
            return user_input
        print("Oops! That was an empty string. Try again...")


def ask_for_option_within_list(names_list):
    selected_index = 0

    while not 0 < selected_index <= len(names_list):

        display_list(names_list)
        selected_index = get_user_input_integer(
            "Enter the number of the name you want to change: "
        )

        print("Oops! Please select a number within the list. Try again...")

    return selected_index - 1


def handle_operations(names_list, operation):
    if not names_list:
        print("The list is empty, you can't perform this operation")
        return

    selected_index = ask_for_option_within_list(names_list)

    if operation == "DELETE_NAME":
        names_list = delete_name(names_list, selected_index)
    elif operation == "CHANGE_NAME":
        new_name = get_user_input_string("Enter a new name: ")
        names_list = change_name(names_list, selected_index, new_name)


def display_list(names_list):
    print("Here's the current list:")
    # Enumerate allows to loop through the elements of the list.
    for counter, name in enumerate(names_list, 1):
        print(f"{counter}) {name}")


def add_name(names_list, name):
    names_list.append(name)
    return names_list


def change_name(names_list, selected_index, new_name):
    names_list[selected_index] = new_name
    return names_list


def delete_name(names_list, selected_index):
    del names_list[selected_index]
    return names_list


def view_names(names_list):
    if not names_list:  # Check if list is empty
        print("The list is empty")
    else:
        display_list(names_list)


def challenge_121():
    names_list = []

    while True:
        print(
            """
            Please select one of the following options:
            1) Add a name
            2) Change a name
            3) Delete a name
            4) View names
            5) Quit program
            """
        )

        user_choice = input("What do you want to do? ")
        if user_choice == "1":
            name = get_user_input_string("Enter a new name: ")
            names_list = add_name(names_list, name)
        elif user_choice == "2":
            handle_operations(names_list, "CHANGE_NAME")
        elif user_choice == "3":
            handle_operations(names_list, "DELETE_NAME")
        elif user_choice == "4":
            view_names(names_list)
        elif user_choice == "5":
            print("Exiting program...")
            sys.exit()  # terminate program
        else:
            print("Incorrect option, please try again: ")


if __name__ == "__main__":
    challenge_121()

