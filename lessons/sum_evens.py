"""Practice summing over lists."""

def sum_evens_in_list(input_list: list[int]) -> int:
    """Sum all even numbers in this list."""
    list_sum: int = 0
    for elements in input_list:
        if elements % 2 == 0:
            list_sum += elements
    return list_sum