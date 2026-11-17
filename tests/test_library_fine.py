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
def test_calculate_fine_returns_fine(days_overdue, expected_fine):

    fine = calculate_fine(days_overdue)

    assert fine == expected_fine
    assert type(fine) is int


@pytest.mark.parametrize("invalid_value",["1",1.5,None,True])
def test_calculate_fine_rejects_invalid_types(invalid_value):

    with pytest.raises(TypeError):
        calculate_fine(invalid_value)


def test_calculate_fine_rejects_negative_days():

    with pytest.raises(ValueError):
        calculate_fine(-1)
