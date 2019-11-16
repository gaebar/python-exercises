# Challenge 048
again = "y"
count = 0
while again == "y":
    name = input("What's your guest name? ")
    print(name, "has now been invited to the party!")
    count = count + 1
    again = input("Do you want to invite someonelse? (y/n) ")
print("Oooh! There will be", count, "happy people at the party!")
