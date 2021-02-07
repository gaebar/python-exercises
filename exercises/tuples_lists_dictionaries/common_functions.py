def get_user_input_integer(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        print(f"Oops! {user_input} is not a valid number. Try again...")
