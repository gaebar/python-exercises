# TUPLES, LISTS AND DICTIONARIES

"""
Create a list of six school subjects. Ask the user which of these subjects they don't like. 
Delete the subject they have chosen from the list before you display the list again.
"""

subjects_list = ["Maths", "Literature", "Science", "History", "Spanish", "Computing"]


def join_subjects(subjects_list):
    return ", ".join(subjects_list)


print(f"Subjects list: {join_subjects(subjects_list)}")


def ask_user_input():
    while True:
        user_input = input("Which one of these subjects do you dislike? ")
        if user_input in subjects_list:
            erase_from_list = subjects_list.index(user_input)
            del subjects_list[erase_from_list]

            print(f"{user_input} is no more in the subject list!")
            print(f"New subjects list: {join_subjects(subjects_list)}")
            return

        print(f"{user_input} is not in the list. Try again!")


ask_user_input()
