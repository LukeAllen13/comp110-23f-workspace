"""for loop practice in class."""


def w_sum(nums: list[int]) -> int:
    """sums each integer in an inputed list."""
    assert len(nums) > 0
    i = 0
    sum: int = 0
    while i < len (nums):
        sum: int = sum + nums[i]
        i += 1
    return sum


def f_sum(nums: list[int]) -> int:
    """sums each integer in an inputed list."""
    assert len(nums) > 0
    sum: int = 0
    for num in nums:
        sum += num
    return sum


print("Input a list of ints into the function f_range_sum. Try to input ints that add up to my mystery lucky number!")
def f_range_sum(nums: list[int]) -> int or str:
    """sums each index in an inputed list."""
    assert len(nums) > 0
    lucky_number = 13
    sum: int = 0
    for idx in range(0, len(nums)):
        sum += nums[idx]
    if sum == lucky_number:
        return "YOU FOUND MY LUCKY NUMBER!!"
    if sum != lucky_number:
        return (f"Try again! My lucky number is not {sum}")