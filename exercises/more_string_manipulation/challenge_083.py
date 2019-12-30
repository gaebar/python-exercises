# MORE STRING MANIPULATION CHAPTER
# Challenge 083
"""
Ask the user to type in a word in upper case. If they type it in lower case,
ask them to try again. Keep repeating this until they type in a message all 
in uppercase.
"""


def check_if_uppercase(message):
    if message.isupper():
        return True
    else:
        return False


def prompt_for_user_message():
    enter_message_string = "Enter a message in uppercase: "
    should_stop = False
    while not should_stop:
        message = input(enter_message_string)
        if check_if_uppercase(message):
            print("Thank you!")
            should_stop = True
        else:
            print("Please, try again")


if __name__ == "__main__":
    prompt_for_user_message()
