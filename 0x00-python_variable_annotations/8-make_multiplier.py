#!/usr/bin/env python3
"""typing callables"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def multiply(num: float) -> float:
        """the function"""
        return num * multiplier
    return multiply
