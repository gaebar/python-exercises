# MORE STRING MANIPULATION CHAPTER

# Challenge 082
"""
Show the user a line of text from your favourite poem and ask for a starting
and ending point. Display the characters between those two points.
"""


def trim_characters(poem, start, end):
    length_poem = len(poem)
    if length_poem < start:
        raise IndexError("list index out of range")

    if isinstance(start, int) and isinstance(end, int):
        if start > 0 and end >= start:
            user_line_choose = poem[start:end]
            return user_line_choose
        else:
            raise TypeError("Input indexes are out of range")
    else:
        raise TypeError("Input indexes are not numeric")


def display_line():
    poem = "Oh, I wish I'd looked after me teeth,"
    start = int(input("Enter a starting number: "))
    end = int(input("Enter an ending number: "))

    trimmed_poem = trim_characters(poem, start, end)

    print(trimmed_poem)


if __name__ == "__main__":
    display_line()

