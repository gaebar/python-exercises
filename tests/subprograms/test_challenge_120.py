import pytest

from exercises.subprograms import challenge_120

TEST_DATA = [(3, 10, "+", 13), (3, 7, "+", 10), (0, 0, "+", 0), (10, 5, "-", 5)]

TEST_DATA_ERROR = [(3, 10, "+", 10), (0, 0, "+", 10), (10, 5, "-", 15)]

TEST_PARAMETERS = "num_1, num_2, operation, user_answer"

@pytest.mark.parametrize(TEST_PARAMETERS, TEST_DATA)
def test_operation_success(num_1, num_2, operation, user_answer):
    (check_result, correct_response) = challenge_120.check_answer(
        num_1, num_2, operation, user_answer
    )

    assert check_result


@pytest.mark.parametrize(TEST_PARAMETERS, TEST_DATA_ERROR)
def test_operation_error(num_1, num_2, operation, user_answer):
    (check_result, correct_response) = challenge_120.check_answer(
        num_1, num_2, operation, user_answer
    )
    assert not check_result
