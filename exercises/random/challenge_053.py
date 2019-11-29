### RANDOM CHALLENGE ###

"""
053
Display a random fruit from a list of five fruits
"""
import random


def get_random_choice(input_array):
    return random.choice(input_array)


print(get_random_choice(["apple", "pear", "peach", "banana", "mango"]))
