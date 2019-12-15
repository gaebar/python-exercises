from exercises.more_string_manipulation import challenge_080


def test_processing():
    # Define inputs
    test_first_name = "Marco"
    test_last_name = "Barr"

    # invoke function with the test inputs
    full_name = challenge_080.processing(test_first_name, test_last_name)

    # verify that function output is as expected
    assert full_name == "Marco Barr"


def test_length_of():
    name = "Richard"
    output = challenge_080.length_of(name)
    assert output == len(name)
