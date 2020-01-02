# CHALLENGE 071
"""
Create a list of two sports. Ask the user what their favourite sport is and add this to the end of the list. 
Sort the list and display it.
"""

sport_list = ["football", "basket-ball"]
sport_list.append(input("What is your favourite sport? "))
# .sort return the list in alphabetical order
sport_list.sort()
print(sport_list)
