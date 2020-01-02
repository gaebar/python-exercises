# Challenge 049
compnum = 50
num = int(input("Enter a number: "))
count = 1
while num != compnum:
    if num < compnum:
        print("Too low")
    else:
        print("Too high")
    count = count + 1
    num = int(input("Have another go: "))
print("Well done, mate! You took", count, "attempts!")
