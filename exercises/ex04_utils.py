"""EX04 - List Utility Functions!"""
__author__ = "730704135"

def all(int_list: list[int], single_int: int) -> bool:
    """Given a list of integers and a sngle integer, check to see if the list contains only the single integer. If so, return True, if not, return False."""
    i = 0
    while i < int(len(int_list)):
        if str(int_list[i]) == str(single_int):
            i += 1
        else:
            return False
    return True

def max(ints: list[int]) -> int:
    """Given a list of integers, return the integer that is the largest."""
    i = 0
    max_int:int = 0
    if len(ints) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(ints) - 1:
        if ints[i + 1] > ints[i]:
            max_int = int[i + 1]
        i += 1


