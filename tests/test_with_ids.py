"""
Script: test_with_ids.py
"""

import pytest


@pytest.mark.parametrize("input_data,expected", [
    ([1, 2, 3, 4], 2.5),    # positive numbers
    ([0, 0, 0, 0], 0),      # zeros
    ([5], 5),               # single value
], ids=["positive_numbers", "zeros", "single_value"])
def test_mean_with_ids(input_data, expected):
    assert sum(input_data) / len(input_data) == expected
