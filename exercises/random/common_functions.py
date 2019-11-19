# Ask for user input and ensuring the user entering an integer
def get_user_input(message):
    while(True):
        user_input = input(message)
        if not user_input.isdigit():
            print("Oops! That was not a valid number. Try again...")
        else:
            return int(user_input)