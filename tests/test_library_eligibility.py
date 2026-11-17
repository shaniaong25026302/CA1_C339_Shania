import pytest

from library_eligibility import can_borrow


@pytest.mark.parametrize(
    "active_loans, overdue_books, expected_fine",
    [
        (0, 0, True),
        (4, 0, True),
        (5, 0, False),
        (6, 0, False),
        (4, 1, False),
        (5, 1, False),
    ]
)
def test_can_borrow_returns_eligibility(active_loans, overdue_books, expected_fine):
    result = can_borrow(active_loans, overdue_books)

    assert result is expected_fine


@pytest.mark.parametrize("invalid_value", ["1", 1.5, None, True])
def test_can_borrow_rejects_invalid_active_loan_types(invalid_value):

    with pytest.raises(TypeError):
        can_borrow(invalid_value, 0)


@pytest.mark.parametrize("invalid_value", ["1", 1.5, None, True])
def test_can_borrow_rejects_invalid_overdue_books_types(invalid_value):

    with pytest.raises(TypeError):
        can_borrow(0, invalid_value)


@pytest.mark.parametrize(
    "active_loans, overdue_books",
    [
        (-1, 0),
        (0, -1),
    ]
)
def test_can_borrow_rejects_negative_values(active_loans, overdue_books):

    with pytest.raises(ValueError):
        can_borrow(active_loans, overdue_books)
