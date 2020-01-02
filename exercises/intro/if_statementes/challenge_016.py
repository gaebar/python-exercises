# Challenge 016
user = input("It is raining outside? ")
user = str.lower(user)
if user == "yes":
    windy = input("Is it windy? ")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella!")
    else:
        print("Take an umbrella!")

else:
    print("Enjoy your day!")
