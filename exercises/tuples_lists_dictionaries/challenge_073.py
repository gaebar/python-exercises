# TUPLES, LISTS AND DICTIONARIES

# Challenge 073
"""
Ask the user to enter four of their favourite foods and store them in a dictionary 
so that they are indexed with numbers starting from 1. Display the dictionary in full, 
showing the index number and the item. Ask them which they want to get rid of and 
remove it from the list. Sort the remaining data and display the dictionary.
"""

food_prompts = [
    "What's your first food item? ",
    "What's your second food item? ",
    "What's your third food item? ",
    "What's your fourth food item? ",
]


def get_user_input(message):
    while True:
        user_input = input(message)
        if len(user_input) == 0:
            print("Please enter a food name.")
        return user_input


def get_user_input_integer(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        print("Oops! That was not a valid number. Try again...")


def ask_for_user_foods():
    food_dictionary = {}

    index = 0
    for food in food_prompts:
        food_dictionary[index] = get_user_input(food)
        index += 1

    return food_dictionary


def remove_unwanted_food(food_dictionary):
    while True:
        user_input = get_user_input_integer(
            "What's the food you would like to remove? "
        )
        if user_input in food_dictionary:
            del food_dictionary[user_input]
            return food_dictionary
        else:
            print("This integer is not in the list")


def processing(food_dictionary):
    removed_food_dictionary = remove_unwanted_food(food_dictionary)
    return sorted(removed_food_dictionary.values())


def challenge_73():
    food_dictionary = ask_for_user_foods()
    print(food_dictionary)

    sorted_dictionary = processing(food_dictionary)
    print(sorted_dictionary)


if __name__ == "__main__":
    challenge_73()

# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
