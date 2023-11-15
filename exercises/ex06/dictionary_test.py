"""Let's test our dictionary utils!"""

__author__ = "730704135"

import pytest
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert1():
    """Test KeyError inside invert."""
    with pytest.raises(KeyError):
        my_dictionary: dict[str, str] = {"alyssa": "byrnes", "adam": "byrnes"}
        invert(my_dictionary)


def test_invert2():
    """Test to see if invert works on test dictionary."""
    test_dict: dict[str, str] = {"Hello" : "Bye", "Bye" : "Hello"}
    assert invert(test_dict) == {"Bye" : "Hello", "Hello" : "Bye"}


def test_invert3():
    """Test another dict to see if invert works."""
    test_dict: dict[str, str] = {"Bye": "Hello", "Good": "Talk", "Hello": "Do"}
    assert invert(test_dict) == {"Hello": "Bye", "Talk": "Good", "Do": "Hello"}


def test_fav_color_use1():
    """Test to see if favorite color is returned."""
    test_dict: dict[str, str] = {"Luke": "Blue", "Manix": "Orange", "David": "Blue"}
    assert favorite_color(test_dict) == "Blue"


def test_fav_color_use2():
    """Test to see if favorite color is returned in a different dict."""
    test_dict: dict[str, str] = {"Luke": "Orange", "David": "White", "Tyler": "Pink", "Jake": "Black", "Nathan": "Pink"}
    assert favorite_color(test_dict) == "Pink"


def test_fav_color_edge():
    """Test to make sure an empty inputed dictionary doesn't make an error."""
    assert favorite_color({}) == "Input is empty! Please enter a dictionary."


def test_count_use1():
    """Test to see if terms are counted correctly."""
    test_list: list[str] = ["Hello", "Hello", "Hello", "See", "See", "See"]
    assert count(test_list) == {'Hello': 3, 'See': 3}


def test_count_use2():
    """Test to see if terms are counted correctly in a different inputed list."""
    test_list: list[str] = ["One_Very_Very_Very_Very_Very_Long_Term"]
    assert count(test_list) == {"One_Very_Very_Very_Very_Very_Long_Term": 1}


def test_count_edge():
    """Test to make sure an empty inputed list doesn't make an error."""
    assert count([]) == {}


def test_alphabet_use1():
    """Test to see if the keys are set equal to the first letter of the value words."""
    test_list: list[str] = ["Apple", "able", "Bell", "Car", "Door"]
    assert alphabetizer(test_list) == {'a': ['Apple', 'able'], 'b': ['Bell'], 'c': ['Car'], 'd': ['Door']}


def test_alphabet_use2():
    """Test to see if an alternate list correctly."""
    test_list: list[str] = ["AAA", "AAAA", "AAAAA"]
    assert alphabetizer(test_list) == {'a': ['AAA', 'AAAA', 'AAAAA']}


def test_alphabet_edge():
    """Test to make sure an empty inputed list doesn't make an error."""
    assert alphabetizer([]) == {}


def test_attendance_use1():
    """Test to see if the attendance is marked correctly."""
    assert update_attendance({"monday": ["david", "luke"]}, "monday", "manix") == {"monday": ["david", "luke", "manix"]}


def test_attendance_use2():
    """Test to see if the attendance is marked correctly."""
    assert update_attendance({"tuesday": ["manix", "luke"]}, "tuesday", "david") == {"tuesday": ["manix", "luke", "david"]}


def test_attendance_edge():
    """Test to make sure an empty attendance does not give errors."""
    assert update_attendance({}, "Monday", "Luke") == {"Monday": ["Luke"]}

