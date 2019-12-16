# What are you raising here?

import pytest
from exercises.more_string_manipulation import challenge_082


def test_trim_characters():
    poem = "All the world's a stage"
    start = 3
    end = 10

    trimmed_poem = challenge_082.trim_characters(poem, start, end)

    assert trimmed_poem == " the wo"

