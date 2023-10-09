"""EX04 - List Utility Functions!"""
__author__ = "730704135"


def all(int_list: list[int], single_int: int) -> bool:
    """Given a list of integers and a sngle integer, check to see if the list contains only the single integer. If so, return True, if not, return False."""
    i = 0
    # uses the index counter i to go through each index of the inputed list, checking to see if the inputed int is the same as each
    while i < int(len(int_list)):
        if str(int_list[i]) == str(single_int):
            i += 1
        else:
            return False
    return True


def max(ints: list[int]) -> int:
    """Given a list of integers, return the integer that is the largest."""
    i = 0
    # uses the index counter i to go through each int in the list and compare it to the int in the next index. 
    # I did len (ints) -1 because you dont need to compare the int of the second to last index to anything if you already have the resulting info.
    if len(ints) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(ints) - 1:
        if ints[i] > ints[i + 1]:
            max_int = ints[i]
        else:
            max_int = ints[i + 1]
        i += 1
    return max_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists of integers, return True is the lists are exactly the same."""
    i = 0
    # uses the index counter i to go through each index in both lists and makes sure each int is equal before returning True.
    if len(list1) != len(list2):
        return False
    while i < len(list1):
        if list1[i] == list2[i]:
            i += 1
        else:
            return False
    return True