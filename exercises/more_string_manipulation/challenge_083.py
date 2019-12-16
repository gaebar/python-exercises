# MORE STRING MANIPULATION CHAPTER

# Challenge 083
"""
Ask the user to type in a word in upper case. If they type it in lower case,
ask them to try again. Keep repeating this until they type in a message all 
in uppercase.
"""
# Input
# Processing
# Output


def check_if_uppercase(message):
    try_again = False
    while try_again == False:
        if message[0].isupper():
            print("Thank you!")
            try_again = True
        else:
            print("Please, try again")
            message = input("Enter a message in uppercase: ")
        return try_again


def user_message():
    # INPUT
    message = input("Enter a message in uppercase: ")

    # PROCESSING
    uppercase = check_if_uppercase(message)

    # OUTPUT
    print(uppercase)


if __name__ == "__main__":
    user_message()


# # ORIGINAL
# message = input("Enter a message in uppercase: ")
# try_again = False
# while try_again == False:
#     if message[0].isupper():
#         print("Thank you!")
#         try_again = True
#     else:
#         print("Please, try again")
#         message = input("Enter a message in uppercase: ")
