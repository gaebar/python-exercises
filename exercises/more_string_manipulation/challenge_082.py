# MORE STRING MANIPULATION CHAPTER

# Challenge 082
"""
Show the user a line of text from your favourite poem and ask for a starting
and ending point. Display the characters between those two points.
"""


def trim_characters(poem, start, end):
    user_line_choose = poem[start:end]
    return user_line_choose


def display_line():
    poem = "Oh, I wish I'd looked after me teeth,"
    start = int(input("Enter a starting number: "))
    end = int(input("Enter an ending number: "))

    trimmed_poem = trim_characters(poem, start, end)

    print(trimmed_poem)


if __name__ == "__main__":
    display_line()

