# Challenge 042
total = 0
for i in range(0, 5):
    num = int(input("Enter a number and the computer will calculate the result: "))
    ans = input("Do you want this number included? (y/n) ")
    if ans == "y":
        total = total + num
print(total)
