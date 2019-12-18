# MORE STRING MANIPULATION

# Challenge 081
"""
Ask the user to type their favourite school subject.
Display it with "-" after each letter, e.g S-p-a-n-i-s-h-.
"""


def processing(subject):
    letters = list(subject)
    joined_subject = f"{'-'.join(letters)}-"

    return joined_subject


def favourite_subject():
    subject = input("Enter your favourire school subject: ")
    result = processing(subject)
    print(result)


if __name__ == "__main__":
    favourite_subject()
