# Challenge 043
name = input("Which direction want to count (up or down)? : ")
if name == "up":
    num_top = int(input("Please, enter the top number: "))
    for i in range(1, num_top + 1):
        print(i)

elif name == "down":
    num_below = int(input("Please, enter a number below 20: "))
    for i in range(20, num_below - 1, -1):
        print(i)
else:
    print("I don't understand")
