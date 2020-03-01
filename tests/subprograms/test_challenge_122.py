from exercises.subprograms import challenge_122

import csv
import random
import os


def test_challenge_122_add():
    input_name = "Test Name"
    input_salary = "1000"

    # Ensure we don't overwrite an existing file in the folder
    test_csv_file_name = f"SalariesTest_{random.randint(100, 100000)}.csv"
    FIELD_NAMES = ["name", "salary"]

    challenge_122.add_to_file_CSV_writer(
        input_name, input_salary, test_csv_file_name, FIELD_NAMES
    )

    with open(test_csv_file_name, newline="") as file:
        reader = csv.reader(file)
        os.remove(test_csv_file_name)
        for row in reader:
            assert row == [input_name, input_salary]

