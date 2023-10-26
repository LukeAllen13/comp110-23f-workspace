"""Combining two lists into a dictionary."""
__author__ = "730704135"


def zip(key: list[str], value: list[int]) -> dict[str, int]:
    """Assign values to keys which are inputs through 2 lists using the function zip."""
    zippy: dict[str, int] = {}
    if len(key) and len(value) == 0:
        return zippy
    if len(key) != len(value):
        return zippy
    i = 0
    while i < len(key):
        zippy[f"{key[i]}"] = value[i]
        i += 1
    return zippy