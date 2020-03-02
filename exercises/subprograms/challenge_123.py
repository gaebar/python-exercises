"""
In Python, it is not technically possible to directly delete
a record from a .csv file. Instead you need to save the file to
a temporary list in Python, make the changes to the list and
then overwrite the original file with the temporary list.

Change the previous program to allow you to do this. Your menu
should now look like this:

1) Add to file
2) View all records
3) Delete a record
4) Quit program

Enter the number of your selection:
"""

import csv
import sys
import os.path
import locale

locale.setlocale(locale.LC_ALL, "en_GB")

CSV_FILE_NAME = "Salaries.csv"
FIELD_NAMES = ["name", "salary"]


def get_user_input_integer(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        print("Oops! That was not a valid number. Try again...")


def get_row_within_array(message, list):
    while True:
        user_index = get_user_input_integer(message)
        if 0 < user_index <= len(list):
            return user_index
        print("Oops! That was not a valid row number. Try again...")


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
    add_to_file_CSV_writer(name, salary, CSV_FILE_NAME, FIELD_NAMES)


def add_to_file_CSV_writer(name, salary, CSV_FILE_NAME, FIELD_NAMES):
    with open(CSV_FILE_NAME, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        writer.writerow({FIELD_NAMES[0]: name, FIELD_NAMES[1]: salary})


def view_records():
    if not csv_file_exists():
        return

    with open(CSV_FILE_NAME, newline="") as file:
        print("\nCurrent Records:")
        reader = csv.reader(file)

        for row in reader:
            salary = float(row[1])
            print(f"{reader.line_num}) {row[0]}, {locale.currency(salary, True, True)}")

        if reader.line_num == 0:
            print("No records to display")


def csv_file_exists():
    if os.path.exists(CSV_FILE_NAME):
        return True

    print("There are no records to display.")
    return False


def delete_record():
    if not csv_file_exists():
        return

    temporary_list = []

    view_records()

    with open(CSV_FILE_NAME, newline="") as file:
        reader = csv.DictReader(file, FIELD_NAMES)
        for row in reader:
            temporary_list.append(row)

    row_to_delete = get_row_within_array(
        "Enter the number of the row to delete: ", temporary_list
    )

    delete_record_dict_writer(temporary_list, row_to_delete, CSV_FILE_NAME)

    view_records()


def delete_record_dict_writer(temporary_list, row_to_delete, CSV_FILE_NAME):
    del temporary_list[row_to_delete - 1]
    with open(CSV_FILE_NAME, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        for row in temporary_list:
            writer.writerow({"name": row["name"], "salary": row["salary"]})


def challenge_123():
    while True:
        print(
            """
            Please select one of the following options:
            1) Add to file
            2) View all records
            3) Delete a record
            4) Quit program
            """
        )

        user_choice = input("Enter the number of your selection: ")
        if user_choice == "1":
            add_to_file()
        elif user_choice == "2":
            view_records()
        elif user_choice == "3":
            delete_record()
        elif user_choice == "4":
            print("Exiting program...")
            sys.exit()
        else:
            print("Incorrect option, please try again: ")


if __name__ == "__main__":
    challenge_123()
