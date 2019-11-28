# TUPLES, LISTS AND DICTIONARIES

"""
Create a list of six school subjects. Ask the user which of these subjects they don't like. 
Delete the subject they have chosen from the list before you display the list again.
"""

subjects_list = ["Maths", "Literature", "Science", "History", "Spanish", "Computing"]
print(subjects_list)
dislike = input("Which of these subjects do you dislike? ")
erase_from_list = subjects_list.index(dislike)
del subjects_list[erase_from_list]
print(subjects_list)

