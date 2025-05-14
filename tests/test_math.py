import pytest
from src.math import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (0, 1, 1),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
