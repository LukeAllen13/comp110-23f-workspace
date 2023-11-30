"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730704135"


class Simpy:
    """Simpy."""
    values: list[float]

    def __init__(self, val_list: list[float]):
        """Constructor."""
        self.values = val_list

    def __str__(self) -> str:
        """Magic!"""
        return f"Simpy({self.values})"

    def fill(self, val: float, num_vals: int) -> None:
        """Fill."""
        cur_len = len(self.values)
        if num_vals > cur_len:
            while len(self.values) < num_vals:
                self.values.append(val)
        elif num_vals < cur_len:
            while len(self.values) > num_vals:
                self.values.pop()

    def arange(self, start: float, stop: float, step: Union[float, None] = 1.0) -> None:
        """Arange."""
        if step is None:
            step = 1.0

        if step == 0.0:
            raise ValueError("Step cannot be 0!!!")

        if start < stop and step > 0:
            my_val = start
            while my_val < stop:
                self.values.append(my_val)
                my_val += step
        elif start > stop and step < 0:
            my_val = start
            while my_val > stop:
                self.values.append(my_val)
                my_val += step
        else:
            raise ValueError("Invalid parameters for the method: arange.")

    def sum(self) -> float:
        """Sum."""
        summing_int: float = 0.0
        for i in self.values:
            summing_int += i
        return summing_int

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Union add."""
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            added_vals = [self.values[i] + rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            added_vals = [i + rhs for i in self.values]
        else:
            raise TypeError(f"Operand type is not allowed for +: {type(rhs)}")
        return Simpy(added_vals)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise to a power."""
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            power_vals = [self.values[i] ** rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            power_vals = [i ** rhs for i in self.values]
        else:
            raise TypeError(f"Operand type is not allowed for **: {type(rhs)}")
        return Simpy(power_vals)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a 'mask'."""
        mask: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            mask = [self.values[i] == rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            mask = [value == rhs for value in self.values]
        else:
            raise TypeError(f"Operand type is not allowed for ==: {type(rhs)}")
        return mask  

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Lets make another mask but to see if the values are greater than."""
        mask: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            mask = [self.values[i] > rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            mask = [value > rhs for value in self.values]
        else:
            raise TypeError(f"Operand type is not allowed for >: {type(rhs)}")
        return mask  

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allow for subscription notation to be used as well as the second usage with the list[bool]."""
        sub_list: list[float] = self.values
        item_list: list[float] = []
        if isinstance(rhs, int):
            return sub_list[rhs]
        elif isinstance(rhs, list):
            assert len(rhs) == len(self.values)
            for i in range(len(rhs)):
                if rhs[i]:
                    item_list.append(self.values[i])
            return Simpy(item_list)
