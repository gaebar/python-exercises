# Challenge 044
num = int(input("How many people do you want to invite to the party? "))
if num < 10:
    for i in range(0, num):
        name = input("Please, enter the name: ")
        print("Success!", name, "has been added to the party list!")
else:
    print("Too many people, sorry! The guests number should be less then 10")

## WHILE LOOP CHALLENGES ###
