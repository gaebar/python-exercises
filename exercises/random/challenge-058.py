### RANDOM CHALLENGE ###

"""
058
Make a maths quiz that asks five questions by randomly generating two whole number 
to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer.
If they get it right add a point to the score. At the end of the quiz, 
tell them how many they got correct out of five.  
"""
import random
score = 0
print("Back to school, test your maths!")
for i in range(1,2):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    sum = num1 + num2
    print(num1, "+", num2, "=")
    answer = int(input("Your answer: "))
    print()
    if answer == sum:
        score = score +1
for i in range(1,2):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    sum = num1 / num2
    print(num1, ":", num2, "=")
    answer = float(input("Your answer: "))
    print()
    if answer == sum:
        score = score +1
for i in range(1,3):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    sum = num1 * num2
    print(num1, "x", num2, "=")
    answer = int(input("Your answer: "))
    print()
    if answer == sum:
        score = score +1
for i in range(1,2):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    sum = num1 - num2
    print(num1, "-", num2, "=")
    answer = int(input("Your answer: "))
    print()
    if answer == sum:
        score = score +1

if score == 5:
    print ("You rock! 5 out of 5!")
else: 
    print ("You scored", score, "out of 5")