# # Python by Example Book - exercises

### IF STATEMENTS CHALLENGES ###

# # Challenge 012
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print(num2, num1)
# else:
#     print(num1, num2)

# # Challenge 013
# num = int(input("Enter a number that is under 20: "))
# if num > 20:
#     print("The number you entered is too high. Pleas43e, try again!")
# else:
#     print("Thank you!")

# Challenge 014
# num = int(input("Please, enter a number between 10 and 20 - inclusive: "))
# if num >= 10 and num <= 20:
#     print("Thank you!")
# else:
#     print("Incorrect answer")

# # Challenge 015
# color = input("Enter your favorite colour: ")
# if color == "red" or color == "RED" or color == "Red":
#     print("I like red too!")
# else:
#     print("I don't like that color, I prefer red")

# # Challenge 016
# user = input("It is raining outside? ")
# user = str.lower(user)
# if user == "yes":
#     windy = input("Is it windy? ")
#     windy = str.lower(windy)
#     if windy == "yes":
#         print("It is too windy for an umbrella!")
#     else:
#         print("Take an umbrella!")

# else:
#     print("Enjoy your day!")

# # Challenge 017
# age = int(input("How old are you? "))
# if age >= 18:
#     print("You can vote")
# elif age == 17:
#     print("You can learn to drive")
# elif age == 16:
#     print("You can buy a lottery ticket")
# else:
#     print("You can go Trick-or-Treating")

# # Challenge 018
# num = int(input("Enter a number: "))
# if num < 10:
#     print("Too low")
# elif num >= 10 and num <= 20:
#     print("Correct!")
# else:
#     print("Too high")

# # Challenge 019
# num = int(input("Enter the number 1, 2 or 3: "))
# if num == 1:
#     print("Thank you!")
# elif num == 2:
#     print("Well done!")
# elif num == 3:
#     print("Correct")
# else:
#     print("Error messsage")

### STRINGS CHALLENGES ###

# # Challenge 020
# name = input("Enter your name: ")
# length = len(name)
# print(length)

# # Challenge 021
# firstname = input("Enter your name: ")
# lastname = input("Enter you lastname: ")
# name = firstname + " " + lastname
# length = len(name)
# print(name)
# print(length)

# # Challenge 022
# firstname = input("Enter your name in lower case: ")
# lastname = input("Enter you lastname in lower case: ")
# name = firstname + " " + lastname
# cap = name.title()
# print("Your lower case name: ", name)
# print("Here the title case: ", cap)

# # Challenge 023
# rhyme = input(
#     "If you remember it, enter the first line of a nursery rhyme: ")
# length = len(rhyme)
# start_num = int(input("Enter a starting number: "))
# last_num = int(input("Enter a ending number: "))
# part = (rhyme[start_num: last_num])
# print(part)

# # Challenge 024
# word = input("Type any word you like: ")
# upper = word.upper()
# print(upper)

# # Challenge 025
# firstname = input("Please enter your name: ")
# if len(firstname) < 5:
#     surname = input("Enter your surname: ")
#     name = firstname + surname
#     print(name.upper())
# else:
#     print(firstname.lower())

# # Challenge 026
# word = input("Enter a word: ")
# first_word = word[0]
# length = len(word)
# rest = word[1:length]
# if first_word != "a" and first_word != "e" and first_word != "i" and first_word != "o" and first_word != "u":
#     new_word = rest + first_word + "ay"
# else:
#     new_word = word + "way"
# print(new_word.lower())


# # MATHS CHALLENGES
# # Challenge 027 & 028
# num = float(input("Enter a number with lots of decimal places: "))
# answer = num * 2
# print(answer)
# print(round(answer, 2))

# # Challenge 029
# import math
# num = int(input("Enter an integer that is over 500: "))
# answer = math.sqrt(num)
# print(round(answer, 2))

# # Challenge 030
# import math
# print(round(math.pi, 5))

# # Challenge 031
# import math
# radius = int(input("Enter the radius of a circle: "))
# area = math.pi * (radius**2)
# print(area)

# # Challenge 032
# import math
# radius = int(input("Enter the radius of a circle: "))
# depth = int(input("Enter the depth of a cylinder: "))
# area = math.pi * (radius**2)
# total_volume = area * depth
# print(round(total_volume, 3))

# # Challenge 033
# import math
# num1 = int(input("enter a number: "))
# num2 = int(input("enter another number: "))
# div = num1 // num2
# remainder = num1 % num2

# print(num1, "divided by", num2, "is", div, "with", remainder, "remaining")

# # Challenge 034
# print("""
# 1) Square
# 2) Triangle
# """)
# num = (int(input("Enter a number: ")))
# if num == 1:
#     square = int(input("Provide the length of one of the square sides: "))
#     area = square * square
#     print("The area of your square is", area)
# elif num == 2:
#     base = int(input("Provide the base of the triangle: "))
#     height = int(input("and the height of the triangle: "))
#     area = (base * height) / 2
#     print("The area of your triangle is", area)
# else:
#     print("Please, choose a number between the two options")

### FOR LOOP CHALLENGES ###

# # Challenge 035 & 36
# name = input("Enter your name: ")
# num = int(input("Enter a number: "))
# for i in range(0, num):
#     print(name)

# # Challenge 037 & 038
# num = int(input("Enter a number: "))
# name = input("Enter your name: ")
# for x in range(0, num):
#     for i in name:
#         print(i)


# # Challenge 039
# num = int(input("Enter a number between 1 and 12: "))
# for i in range(1, 13):
#     answer = i * num
#     print(i, "x", num, "=", answer)

# # Challenge 040
# import math
# num = int(input("Write a number below 50: "))
# for i in range(50, num - 1, -1):
#     print(i)

# # Challenge 041
# import math
# name = input("Write your name: ")
# num = int(input("Write a number: "))
# if num < 10:
#     for i in range(0, num):
#         print(name)
# else:
#     for i in range(0, 3):
#         print("Too high")

# # Challenge 042
# total = 0
# for i in range(0, 5):
#     num = int(input("Enter a number and the computer will calculate the result: "))
#     ans = input("Do you want this number included? (y/n) ")
#     if ans == "y":
#         total = total + num
# print(total)

# # Challenge 043
# name = input("Which direction want to count (up or down)? : ")
# if name == "up":
#     num_top = int(input("Please, enter the top number: "))
#     for i in range(1, num_top + 1):
#         print(i)

# elif name == "down":
#     num_below = int(input("Please, enter a number below 20: "))
#     for i in range(20, num_below - 1, -1):
#         print(i)
# else:
#     print("I don't understand")

# # Challenge 044
# num = int(input("How many people do you want to invite to the party? "))
# if num < 10:
#     for i in range(0, num):
#         name = input("Please, enter the name: ")
#         print("Success!", name, "has been added to the party list!")
# else:
#     print("Too many people, sorry! The guests number should be less then 10")

### WHILE LOOP CHALLENGES ###

# # Challenge 045
# total = 0
# while total <= 50:
#     num = int(input('Enter a number: '))
#     total = total + num
#     print("The total is ...", num)

# # Challenge 046
# num = 0
# while num <= 5:
#     num = int(input('Enter a number: '))
# print('The last number you entered was a ', num, 'and stop the program')

# # Challenge 047
# num1 = int(input('Enter a number: '))
# total = num1
# again = "y"
# while again == "y":
#     num2 = int(input('Enter another number: '))
#     total = total + num2
#     again = input("Do you want enter another number? (y/n)")
# print("The total is", total)

# # Challenge 048
# again = "y"
# count = 0
# while again == "y":
#     name = input("What's your guest name? ")
#     print(name, "has now been invited to the party!")
#     count = count + 1
#     again = input("Do you want to invite someonelse? (y/n) ")
# print("Oooh! There will be", count, "happy people at the party!")

# # Challenge 049
# compnum = 50
# num = int(input("Enter a number: "))
# count = 1
# while num != compnum:
#     if num < compnum:
#         print("Too low")
#     else:
#         print("Too high")
#     count = count + 1
#     num = int(input("Have another go: "))
# print("Well done, mate! You took", count, "attempts!")

# # Challenge 050
# num = int(input("Enter a number between 10 and 20: "))

# while num < 10 or num > 20:
#     if num < 10:
#         print("Too low!")
#     else:
#         print("Too high")
#     num = int(input("Try again: "))

# print("Thank you!")


# Challenge 051
"""
Using the song “10 green bottles”, display the lines “There are [num] green bottles
hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
should accidentally fall”. Then ask the question “how many green bottles will be
hanging on the wall?” If the user answers correctly, display the message “There will be
[num] green bottles hanging on the wall”. If they answer incorrectly,
display the  message “No, try again” until they get it right. When the number of green
bottles gets  down to 0, display the message “There are no more green bottles
hanging on the wall”.
"""

# count = 10
# while count > 0:
#     print("There are", count, "green bottles hanging on the wall")
#     print(count, "green bottles hanging on the wall, and if 1 green bottle should accidentally fall.")
#     count = count - 1
#     answer = int(input("How many green bottles will be hanging on the wall? "))
#     if answer == count:
#         print("Correct! There will be ", count,
#               "green bottles hanging on the wall.")
#     else:
#         while answer != count:
#             answer = int(input("No, try again: "))
# print("There are no more green bottles hanging on the wall.")
