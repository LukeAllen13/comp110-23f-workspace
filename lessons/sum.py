"""Summing the elements of a list using different loops."""
__author__ = "730704135"


def w_sum(nums: list[float]) -> float:
    """Sums each integer in an inputed list."""
    i = 0
    sum: float = 0
    while i < len(nums):
        sum += + nums[i]
        i += 1
    return sum


def f_sum(nums: list[float]) -> float:
    """Sums each integer in an inputed list."""
    sum: float = 0
    for num in nums:
        sum += num
    return sum


def f_range_sum(nums: list[float]) -> float:
    """Sums each index in an inputed list."""
    sum: float = 0
    for idx in range(0, len(nums)):
        sum += nums[idx]
    return sum