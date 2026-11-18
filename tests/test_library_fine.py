
import pytest

from library_fine import calculate_fine


@pytest.mark.parametrize(
    "days_overdue, expected_fine",
    [
        (0, 0),
        (1, 50),
        (7, 350),
        (9, 450),
        (10, 500),
        (11, 550),
        (30, 1500)
    ]
)
def test_valid_days_overdue_returns_expected_fine(days_overdue, expected_fine):

    fine = calculate_fine(days_overdue)

    assert fine == expected_fine
    assert type(fine) is int


@pytest.mark.parametrize("invalid_value", ["1", 1.5, None, True])
def test_invalid_input_type_raises_type_error(invalid_value):

    with pytest.raises(TypeError):
        calculate_fine(invalid_value)


def test_negative_days_overdue_raises_value_error():

    with pytest.raises(ValueError):
        calculate_fine(-1)
