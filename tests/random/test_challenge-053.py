from exercises.random import challenge_053

# import pytest
# import challenge_053


def test_challenge_053():
    input_array = ["apple", "pear", "peach", "banana", "mango"]
    random_choice = challenge_053.get_random_choice(input_array)
    assert random_choice in input_array
