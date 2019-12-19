import pytest
from exercises.more_string_manipulation import challenge_082

# create a list and then call it
testdata = [
    ("All the world's a stage", 3, 10, " the wo"),
    ("This is a poem", 1, 2, "h"),
    ("This is another poem", 2, 2, ""),
]

testdata_fails = [
    ("All the world's a stage", "hey", "j", TypeError),
    ("", "hey", 2, TypeError),
    ("Poem", 19, 23, IndexError),
]


@pytest.mark.parametrize("poem, start, end, expected", testdata)
def test_trim_characters(poem, start, end, expected):
    # poem = "All the world's a stage"
    # start = 3
    # end = 10

    trimmed_poem = challenge_082.trim_characters(poem, start, end)

    assert trimmed_poem == expected


@pytest.mark.parametrize("poem, start, end, expected", testdata_fails)
def test_trim_characters_fails(poem, start, end, expected):

    with pytest.raises(expected):
        challenge_082.trim_characters(poem, start, end)


# def test_trim_characters(poem, start, end, expected):
# poem = "All the world's a stage"
# start = 3
# end = 10

# trimmed_poem = challenge_082.trim_characters(poem, start, end)

# assert trimmed_poem == expected
