# TUPLES, LISTS AND DICTIONARIES

"""
Create a list of six school subjects. Ask the user which of these subjects they don't like. 
Delete the subject they have chosen from the list before you display the list again.
"""

subjects_list = [
    "Maths",
    "Literature",
    "Science",
    "History",
    "Spanish",
    "Computing",
    "Physics",
    "Geometry",
    "Geography",
    "Economy",
    "Italian",
    "Physical Education",
]
subjects_list_lowercase = [subject.lower() for subject in subjects_list]


def join_subjects(subjects_list):
    return ", ".join(subjects_list)


print(f"Subjects list: {join_subjects(subjects_list)}")


def ask_user_input():
    while True:
        user_input = input("Which one of these subjects do you dislike? ")
        user_input_lowercase = user_input.lower()

        if user_input_lowercase in subjects_list_lowercase:
            index_to_delete = subjects_list_lowercase.index(user_input_lowercase)
            subject_to_delete = subjects_list[index_to_delete]

            del subjects_list[index_to_delete]

            print(f"{subject_to_delete} is not in the subjects list anymore.")
            print(f"New subjects list: {join_subjects(subjects_list)}")
            return

        print(f"{user_input} is not in the list. Try again!")


ask_user_input()
