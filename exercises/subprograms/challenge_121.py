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

import sys


def add_name(names_list):
    name = input("Enter a new name: ")
    names_list.append(name)
    return names_list


def change_name(names_list):
    num = 0
    for x in names_list:
        print(num, x)
        num = num + 1
    select_num = int(input("Enter the number of the name you want to change: "))
    name = input("Enter new name: ")
    names_list[select_num] = name
    return names_list


def delete_name(names_list):
    num = 0
    for x in names_list:
        print(num, x)
        num = num + 1
    select_num = int(input("Enter the number of the name you want to delete: "))
    del names_list[select_num]
    return names_list


def view_names(names_list):
    if len(names_list) == 0:  # Check if list is empty
        print("The list is empty")
    else:
        print("Here are the items in the list:")
        for x in names_list:
            print(f" - {x}")
        print()


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
            names = add_name(names_list)
        elif user_choice == "2":
            names = change_name(names_list)
        elif user_choice == "3":
            names = delete_name(names_list)
        elif user_choice == "4":
            view_names(names_list)
        elif user_choice == "5":
            sys.exit()  # terminate program
        else:
            print("Incorrect option, please try again: ")


if __name__ == "__main__":
    challenge_121()

""" gestire un numero che non esiste, useresti un if?
tipo: if select_num > names:
    print ("The number you entered is not in the index")

"""
