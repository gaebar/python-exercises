### RANDOM CHALLENGE ###

"""
059  
Display five colours and ask the user to pick one. 
If they pick the same as the program has chosen, say "Well done", 
otherwise display a witty answer which involves the correct colour, e.g. "I bet you are GREEN with envy" or 
"Your probably feeling BLUE right now". Ask them to guess again;
if they have still not got it right, keep giving them the same clue 
and ask the user to enter a colour until they guess it correctly.
"""
import random

messages = {
    "red": "Nope! You are probably RED with embarrassment right now",
    "blue": "You are probably feeling BLUE right now",
    "green": "I bet you are GREEN with envy",
    "yellow": "You are probably feeling YELLOW instead of mellow",
    "orange": "I bet you are ORANGE with envy",
}

# messages.keys() converts the dictionary keys to a dict_keys object
# we need to use list() to have an array from it
# https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3
choices = list(messages.keys())

computer_choice = random.choice(choices)

# Converting list to string, by joining each individual list item:
# https://www.programiz.com/python-programming/methods/string/join
joined_choices = ", ".join(choices)
print(f"Pick one of this colours: {joined_choices} ")
colour = True
# added an associate array to avoid the repetition of elif

while colour == True:
    user_pick = input("Your choice: ")
    user_pick = user_pick.lower()

    if user_pick == computer_choice:
        print(f"Well done! {user_pick.capitalize()} is the right colour!")
        colour = False
    elif user_pick in messages.keys():
        print(messages.get(user_pick))
    else:
        print(
            f"{user_pick.capitalize()} is not one of the five given colours. Try again!"
        )
