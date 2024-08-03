#!/usr/bin/env python3
"""typing with unions"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """can be an int or string"""
    return (k, float(v**2))
