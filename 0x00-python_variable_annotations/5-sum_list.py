#!/usr/bin/env python3
"""annoted summing function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """the function it self"""
    sum: float = 0
    for i in input_list:
        sum = sum + i
    return sum
