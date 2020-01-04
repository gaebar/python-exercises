import pytest

from exercises.subprograms import challenge_120

TEST_DATA_ADDITION = [(3, 10, 13), (3, 7, 10), (0, 0, 0)]

TEST_DATA_ADDITION_ERROR = [(3, 10, 10), (0, 0, 10)]


@pytest.mark.parametrize("num_1, num_2, user_answer", TEST_DATA_ADDITION)
def test_addition(num_1, num_2, user_answer):
    (check_result, correct_response) = challenge_120.check_answer_addition(
        num_1, num_2, user_answer
    )
    assert check_result


@pytest.mark.parametrize("num_1, num_2, user_answer", TEST_DATA_ADDITION_ERROR)
def test_addition_error(num_1, num_2, user_answer):
    (check_result, correct_response) = challenge_120.check_answer_addition(
        num_1, num_2, user_answer
    )
    assert not check_result

