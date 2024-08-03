#!/usr/bin/env python3
"""sum of nums lists and ints and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """the summing function"""
    sum: float = 0
    for i in mxd_lst:
        sum = sum + i
    return sum
