# MORE STRING MANIPULATION
from exercises.more_string_manipulation import challenge_081


def test_favourite_subject():
    # Define inputs
    test_subject = "Math"
    test_output = challenge_081.processing(test_subject)
    assert test_output == "M-a-t-h-"
    return


def test_favourite_object_empty_string():
    test_subject = ""
    test_output = challenge_081.processing(test_subject)
    assert test_output == "-"
    return

