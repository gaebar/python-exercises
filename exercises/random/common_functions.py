# Ask for user input and ensuring the user entering an integer
def get_user_input(message):
    while True:
        user_input = input(message)
        if not user_input.isdigit():
            print("Oops! That was not a valid number. Try again...")
        else:
            return int(user_input)


def get_user_input_float(message):
    while True:
        user_input = input(message)
        if not isinstance(eval(user_input), float):
            print("Oops! That was not a valid number. Try again...")
        else:
            return float(user_input)


# # TRY: Ask for user input and ensuring the user entering an integer or a float number
# def get_user_input(message):
#     while True:
#         user_input = input(message)
#         if not user_input.isdigit() or :
#             print("Oops! That was not a valid number. Try again...")
#         else:
#             return int(user_input)

