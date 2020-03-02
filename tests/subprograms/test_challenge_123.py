from exercises.subprograms import challenge_123

import csv
import random
import os


def test_challenge_123_add():
    input_name = "Test Name"
    input_salary = "1000"

    # Ensure we don't overwrite an existing file in the folder
    test_csv_file_name = f"SalariesTest_{random.randint(100, 100000)}.csv"
    FIELD_NAMES = ["name", "salary"]

    challenge_123.add_to_file_CSV_writer(
        input_name, input_salary, test_csv_file_name, FIELD_NAMES
    )

    with open(test_csv_file_name, newline="") as file:
        reader = csv.reader(file)
        os.remove(test_csv_file_name)
        for row in reader:
            assert row == [input_name, input_salary]


def test_challenge_123_delete():
    test_csv_file_name = f"SalariesTest_{random.randint(100, 100000)}.csv"
    row_to_delete = 1
    input_name = "Test Name"
    input_salary = "1000"
    FIELD_NAMES = ["name", "salary"]

    # Add two lines to an empty CSV file
    challenge_123.add_to_file_CSV_writer(
        input_name, input_salary, test_csv_file_name, FIELD_NAMES
    )
    challenge_123.add_to_file_CSV_writer(
        input_name, input_salary, test_csv_file_name, FIELD_NAMES
    )

    # Check that the created CSV file has two lines
    with open(test_csv_file_name, newline="") as file:
        assert len(file.readlines()) == 2

    # Creates a temporary list, one of its items will be removed
    temporary_list = []
    with open(test_csv_file_name, newline="") as file:
        reader = csv.DictReader(file, FIELD_NAMES)
        for row in reader:
            temporary_list.append(row)

    # Deletes one item from the list
    challenge_123.delete_record_dict_writer(
        temporary_list, row_to_delete, test_csv_file_name
    )

    # Checks that there is only one element left
    with open(test_csv_file_name, newline="") as file:
        assert len(file.readlines()) == 1

    # Deletes temporary CSV file
    os.remove(test_csv_file_name)
