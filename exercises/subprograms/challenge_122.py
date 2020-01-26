"""
Create the following menu:
1) Add to file
2) View all records
3) Quit program
Enter the number of your selection:

If the user selects 1, allow them to add to a file called Salaries.csv which
will store their name and salary.

If they select 2 it should display all records in the Salaries.csv file.

If they select 3 it should stop the program. If they select an incorrect option
they should see an error message. They should keep returning to the menu until
they select option 3.
"""

import csv
import sys
import os.path


CSV_FILE_NAME = "Salaries.csv"
FIELD_NAMES = ["name", "salary"]


def get_user_input_float(message):
    while True:
        user_input = input(message)
        try:
            return float(user_input)
        except ValueError:
            print("Oops! That was not a valid number. Try again...")


def get_user_input_string(message):
    while True:
        user_input = input(message)
        if len(user_input) > 0:
            return user_input
        print("Oops! That was not an empty string. Try again...")


def add_to_file():
    name = get_user_input_string("Enter a new name: ")
    salary = get_user_input_float("Enter salary: £")

    with open(CSV_FILE_NAME, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        writer.writerow({FIELD_NAMES[0]: name, FIELD_NAMES[1]: salary})


def view_records():
    if not csv_file_exists():
        return

    with open(CSV_FILE_NAME, newline="") as file:
        reader = csv.reader(file)
        [print(row) for row in reader]


def csv_file_exists():
    if os.path.exists(CSV_FILE_NAME):
        return True

    print("There are no records to display.")
    return False


def challenge_122():
    while True:
        print(
            """
            Please select one of the following options:
            1) Add to file
            2) View all records
            3) Quit program
            """
        )

        user_choice = input("Enter the number of your selection: ")
        if user_choice == "1":
            add_to_file()
        elif user_choice == "2":
            view_records()
        elif user_choice == "3":
            print("Exiting program...")
            sys.exit()
        else:
            print("Incorrect option, please try again: ")


if __name__ == "__main__":
    challenge_122()
