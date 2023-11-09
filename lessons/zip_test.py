"""Tests for the zip function."""
__author__ = "730704135"


from lessons.zip import zip


def test_use_case_1():
    """The inputed key list, when you do len() of that list, should return 2."""
    keys: list[str] = ["Happy", "Tuesday"]
    values: list[int] = [1, 2]
    assert len(zip(keys, values)) == 2


def test_use_case_2():
    """The inputed lists should return a dict: {"Happy": 1, "Tuesday": 2}."""
    keys: list[str] = ["Happy", "Tuesday"]
    values: list[int] = [1, 2]
    assert zip(keys, values) == {"Happy": 1, "Tuesday": 2}


def test_edge_case_1():
    """The inputed lists must be the same length."""
    keys: list[str] = ["Happy", "Tuesday"]
    values: list[int] = [1, 2, 3]
    assert zip(keys, values) == {}


def test_edge_case_2():
    """Test to see if the returned dictionary is empty if the inputed lists are both empty."""
    keys: list[str] = []
    values: list[int] = []
    assert zip(keys, values) == {}
