# MORE STRING MANIPULATION
from exercises.more_string_manipulation import challenge_080


def test_processing():
    # Define inputs
    test_first_name = "Marco"
    test_last_name = "Barr"

    # invoke function with the test inputs
    (
        length_user_first_name,
        length_user_last_name,
        length_full_name,
        full_name,
    ) = challenge_080.processing(test_first_name, test_last_name)

    # verify that function output is as expected
    assert length_user_first_name == len(test_first_name)
    assert length_user_last_name == 4
    assert length_full_name == 10
    assert full_name == "Marco Barr"
