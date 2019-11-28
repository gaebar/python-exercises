# Ask for user input and ensures the user enters an integer
def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        print("Oops! That was not a valid number. Try again...")


# Ask for user input and ensures the user enters a float
def get_user_input_float(message):
    while True:
        user_input = input(message)
        if is_float(user_input):
            return float(user_input)
        print("Oops! That was not a valid number. Try again...")


# Check if the input string is a float
def is_float(value):
    try:
        float(value)
        return True
    except:
        return False
