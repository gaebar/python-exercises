import pytest
from exercises.more_string_manipulation import challenge_082

testdata = [
    ("All the world's a stage", 3, 10, " the wo"),
    ("This is a poem", 1, 2, "h"),
    ("This is another poem", 2, 2, ""),
]

testdata_type_error = [
    ("All the world's a stage", "hey", "j", TypeError),
    ("", "hey", 2, TypeError),
]

testdata_index_error = [
    ("Poem", 19, 23, IndexError),
    ("Another poem", -2, -67, IndexError),
]


@pytest.mark.parametrize("poem, start, end, expected", testdata)
def test_trim_characters(poem, start, end, expected):

    trimmed_poem = challenge_082.trim_characters(poem, start, end)

    assert trimmed_poem == expected


@pytest.mark.parametrize("poem, start, end, expected", testdata_type_error)
def test_trim_characters_type_error(poem, start, end, expected):

    with pytest.raises(expected):
        challenge_082.trim_characters(poem, start, end)


@pytest.mark.parametrize("poem, start, end, expected", testdata_index_error)
def test_trim_characters_index_error(poem, start, end, expected):

    with pytest.raises(expected):
        challenge_082.trim_characters(poem, start, end)
