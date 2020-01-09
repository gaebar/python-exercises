"""
Create the following menu:
1) Add to file
2) View all records
3) Quit program

Enter the number of your selection:

If the user selects 1, allow them to add to a file called Salaries.csv which will
store their name and salary.

If they select 2 it should display all records in the
Salaries.csv file.

If they select 3 it should stop the program. If they select an incorrect option they
should see an error message. They should keep returning to the menu until they select
option 3.
"""

import csv
import sys


def add_to_file():
    file = open("Salaries.csv", "a")
    name = input("Enter a name: ")
    salary = int(input("Enter salary: "))
    new_record = f"{name}, {str(salary)} \n"
    file.write(str(new_record))
    file.close()


def view_records():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()


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

        selection = input("Enter the number of your selection: ")
        if selection == "1":
            add_to_file()
        elif selection == "2":
            view_records()
        elif selection == "3":
            print("Exiting program...")
            sys.exit()  # terminate program
        else:
            print("Incorrect option, please try again: ")


if __name__ == "__main__":
    challenge_122()
