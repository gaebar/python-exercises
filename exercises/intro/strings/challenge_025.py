# Challenge 025
firstname = input("Please enter your name: ")
if len(firstname) < 5:
    surname = input("Enter your surname: ")
    name = firstname + surname
    print(name.upper())
else:
    print(firstname.lower())
