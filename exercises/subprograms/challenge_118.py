"""
Define a subprogram that will ask the user to  enter a number and
save it as the variable “num”. Define another subprogram that will  use “num” and count
from 1 to that number.
"""


def ask_for_number():
    num = int(input("Please, give me a number: "))
    return num


def count_number(num):
    for count in range(1, num + 1):
        print(count)


def challenge_118():
    num = ask_for_number()
    count_number(num)


if __name__ == "__main__":
    challenge_118()

