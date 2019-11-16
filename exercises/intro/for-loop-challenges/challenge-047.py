# Challenge 047
num1 = int(input('Enter a number: '))
total = num1
again = "y"
while again == "y":
    num2 = int(input('Enter another number: '))
    total = total + num2
    again = input("Do you want enter another number? (y/n)")
print("The total is", total)
