"""for loop practice in class."""


def w_sum(nums: list[int]) -> int:
    i = 0
    sum: int = 0
    while i < len (nums):
        sum: int = sum + nums[i]
        i += 1
    return sum


def f_sum(nums: list[int]) -> int:
    sum: int = 0
    for num in nums:
        sum += num
    return sum


def f_range_sum(nums: list[int]) -> int:
    sum: int = 0
    for idx in range(0, len(nums)):
        sum += nums[idx]
    return sum