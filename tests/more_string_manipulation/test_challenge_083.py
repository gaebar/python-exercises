# MORE STRING MANIPULATION CHAPTER

# Challenge 083

import pytest
from exercises.more_string_manipulation import challenge_083

testdata = [
    ("GREAT", True),
    ("it's not great", False),
    ("GreAt", False),
    ("568045", False),
    ("5WER045", True),
    ("IT'S NOT GREAT", True),
    ("", False),
]


@pytest.mark.parametrize("message, expected", testdata)
def test_check_if_uppercase(message, expected):

    is_uppercase = challenge_083.check_if_uppercase(message)

    assert is_uppercase == expected
