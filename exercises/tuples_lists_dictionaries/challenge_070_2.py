# Challenge 069 & 070
"""
69: Create a tuple containing the names of five countries and display the whole tuple.
Ask the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple.

70: Add to program 069 to ask the user a number and display the country in that position.
"""

country_names = ("England", "Italy", "Spain", "France", "Portugal")

print(country_names)
print()
country = input("Please enter one of the countries from above: ")
print(f"{country}, has index number {country_names.index(country)}")
print()
num = int(input("Enter a number between 0 and 4: "))
print(country_names[num])
