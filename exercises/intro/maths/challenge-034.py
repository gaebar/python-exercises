
# Challenge 034
print("""
1) Square
2) Triangle
""")
num = (int(input("Enter a number: ")))
if num == 1:
    square = int(input("Provide the length of one of the square sides: "))
    area = square * square
    print("The area of your square is", area)
elif num == 2:
    base = int(input("Provide the base of the triangle: "))
    height = int(input("and the height of the triangle: "))
    area = (base * height) / 2
    print("The area of your triangle is", area)
else:
    print("Please, choose a number between the two options")
