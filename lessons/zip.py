"""Combining two lists into a dictionary."""
__author__ = "730704135"

def zip(key: list[str], value: list[int]) -> dict[str, int]:
    zippy: dict[str, int] = dict(key, value)
    if len(key) and len(value) == 0:
        return dict()
    if len(key) != len(value):
        return dict()
    i = 0
    while i < len(key):
        zippy[f"{key[i]}"] = value[i]
    return dict