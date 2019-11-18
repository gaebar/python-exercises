### RANDOM CHALLENGE ###

"""
059  
Display five colours and ask the user to pick one. 
If they pick the same as the program has chosen, say "Well done", 
otherwise display a witty answer which involves the correct colour, e.g. "I bet you are GREEN with envy" or 
"Your probably felling BLUE right now". Ask them to guess again;
if they have still not got it right, keep giving them the same clue 
and ask the user to enter a colour until they guess it correctly.
"""
import random
computer_choice = random.choice(["red", "blue", "green", "yellow", "orange"])
print("Pick one of this colours: red, blue, green, yellow, orange")
colour = True
while colour == True:
    user_pick = input("Your choice: ")
    if user_pick == computer_choice:
        user_pick = user_pick.upper()
        print("Well done!", user_pick, "is the right colour!")
        colour = False
    elif user_pick == "red":
        print("Nope! Your probably felling RED right now")
    elif user_pick == "blue":
        print("Your probably felling BLUE right now")
    elif user_pick == "green":
        print("I bet you are GREEN with envy")
    elif user_pick == "yellow":
        print("Your probably felling YELLOW right now")
    elif user_pick == "green":
        print("I bet you are ORANGE with envy")
    else:
        print(user_pick.capitalize(), "is not one of the five given colours. Try again!")

