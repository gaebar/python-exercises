# TUPLES, LISTS AND DICTIONARIES

# Challenge 075
"""
Create a list of four three-digit numbers. Display the list to the user, 
showing each item from list on a separate line. Ask the user to enter
a three-digit number. If the number they have typed in matches one in the list, 
display the position of that number in the list, otherwise display the message
"That is not in the list".
"""

numbers = [123, 345, 234, 765]
for number in numbers:
    print(number)
selection = int(input("Enter a number from the list: "))
if selection in numbers:
    print(f"{selection} is in position {numbers.index(selection)}")
else:
    print("That is not in the list")
