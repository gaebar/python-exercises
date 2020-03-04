import pytest

from exercises.subprograms import challenge_121


test_data_delete = [
    (["name1", "name2", "name3"], 1, ["name1", "name3"]),
    (["name1", "name2", "name3"], 2, ["name1", "name2"]),
]

test_data_delete_error = [
    (["name1", "name2", "name3"], 6, IndexError),
]


test_data_edit = [
    (["name1", "name2", "name3"], 1, "name4", ["name1", "name4", "name3"])
]

test_data_edit_error = [
    (["name1", "name2", "name3"], 6, "name4", IndexError),
]


test_data_add = [
    (["name1", "name2", "name3"], "name4", ["name1", "name2", "name3", "name4"]),
    ([], "name1", ["name1"]),
]


@pytest.mark.parametrize("names_list, index, expected", test_data_delete)
def test_delete_name(names_list, index, expected):

    new_names_list = challenge_121.delete_name(names_list, index)
    assert new_names_list == expected


@pytest.mark.parametrize("names_list, index, expected", test_data_delete_error)
def test_delete_name_error(names_list, index, expected):

    with pytest.raises(expected):
        challenge_121.delete_name(names_list, index)


@pytest.mark.parametrize("names_list, index, new_name, expected", test_data_edit)
def test_edit_name(names_list, index, new_name, expected):

    new_names_list = challenge_121.change_name(names_list, index, new_name)
    assert new_names_list == expected


@pytest.mark.parametrize("names_list, index, new_name, expected", test_data_edit_error)
def test_edit_name_error(names_list, index, new_name, expected):

    with pytest.raises(expected):
        challenge_121.change_name(names_list, index, new_name)


@pytest.mark.parametrize("names_list, new_name, expected", test_data_add)
def test_add_name(names_list, new_name, expected):

    new_names_list = challenge_121.add_name(names_list, new_name)
    assert new_names_list == expected
