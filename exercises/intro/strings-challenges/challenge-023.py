# Challenge 023
rhyme = input(
    "If you remember it, enter the first line of a nursery rhyme: ")
length = len(rhyme)
start_num = int(input("Enter a starting number: "))
last_num = int(input("Enter a ending number: "))
part = (rhyme[start_num: last_num])
print(part)
