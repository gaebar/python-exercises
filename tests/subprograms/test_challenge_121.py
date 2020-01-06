import pytest

from exercises.subprograms import challenge_121


testdata = [["name1", "name2", "name3"], ["name1", "name2"]]


@pytest.mark.parametrize("names_list", testdata)
def test_delete_element(names_list):

    new_names_list = challenge_121.delete_name(names_list, 1)

    assert is_uppercase == expected
