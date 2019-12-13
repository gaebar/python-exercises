# MORE STRING MANIPULATION

# Challenge 081
"""
Ask the user to type their favourite school subject.
Display it with "-" after each letter, e.g S-p-a-n-i-s-h-.
"""


def processing(subject):
    # PROCESSING
    letters = list(subject)
    joined_subject = "-".join(letters) + "-"
    return joined_subject


def favourite_subject():
    # INPUT
    subject = input("Enter your favourire school subject: ")
    result = processing(subject)
    print(result)


if __name__ == "__main__":
    favourite_subject()


# ORIGINAL CODE
# subject = input("Enter your favourire school subject: ")
# for letter in subject:
#     print(letter, end="-")
