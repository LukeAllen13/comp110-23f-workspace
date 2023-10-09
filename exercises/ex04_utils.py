"""EX04 - List Utility Functions!"""
__author__ = "730704135"

def all_same(int_list: list, single_int: int) -> bool:
    """Given a list of integers and a sngle integer, check to see if the list contains only the single integer. If so, return True, if not, return False."""
    i = 0
    while i < int(len(int_list)):
        if str(int_list[i]) == str(single_int):
            i += 1
        else:
            return False
    return True


