"""Define a subprogram that will ask the user to  enter a number and 
save it as the variable  “num”. Define another subprogram that will  use “num” and count 
from 1 to that number. 
"""


def ask_for_number():
    num = int(input("Please, give me a number: "))
    return num


def count_number(num):
    count = 1
    while count <= num:
        print(count)
        count += 1


def challenge_118():
    num = ask_for_number()
    count_number(num)


if __name__ == "__main__":
    challenge_118()

