import sys


def get_user_input_integer(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        print("Oops! That was not a valid number. Try again...")


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
            name = get_user_input_integer("Enter a new name: ")
            names_list = add_name(names_list, name)
        elif user_choice == "2":
            select_index = ask_for_option_within_list(names_list)
            new_name = get_user_input_string("Enter new name: ")
            names_list = change_name(name_list, select_index, new_name)
        elif user_choice == "3":
            select_index = ask_for_option_within_list(names_list)
            names_list = delete_name(names_list, select_index)
        elif user_choice == "4":
            view_names(names_list)
        elif user_choice == "5":
            print("Exiting program...")
            sys.exit()
        else:
            print("Incorrect option, please try again: ")


if __name__ == "__main__":
    challenge_121()
