### RANDOM CHALLENGE ###

"""
055
Randomly choose a number between 1 and 5. Ask the user to pick a number. 
If they guess correctly, display the message "Well done!", otherwise tell them 
if they are too high or too low and ask them to pick a second number. 
If they guess correctly on their second guess, display "Correct",
otherwise dispaly "You lose".
"""
import random
random_num = random.randint(1,5)
user_num = int(input("Pick a number between 1 and 5: "))
if random_num == user_num:
    print ("Well done!")
elif random_num < user_num:
    user_num2 = int(input("Too high! Pick another number: "))
    if random_num == user_num2:
        print("Correct!")
    else:
        print("Sorry, you lose.")
elif random_num > user_num:
    user_num2 = int(input("Too low! Pick another number: "))
    if random_num == user_num2:
        print("Correct!")
    else:
        print("Sorry, you lose.")
    
# Display computer choice
print("Computer choice was", int(random_num))