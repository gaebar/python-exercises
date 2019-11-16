# Challenge 041
import math
name = input("Write your name: ")
num = int(input("Write a number: "))
if num < 10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0, 3):
        print("Too high")
