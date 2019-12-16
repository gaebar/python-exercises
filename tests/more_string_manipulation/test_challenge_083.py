# MORE STRING MANIPULATION CHAPTER

# Challenge 083

from exercises.more_string_manipulation import challenge_083


def test_check_if_uppercase():
    message = "Great!"

    uppercase = challenge_083.check_if_uppercase(message)

    assert message == "Great!"
