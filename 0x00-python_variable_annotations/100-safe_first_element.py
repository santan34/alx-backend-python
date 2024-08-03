#!/usr/bin/env python3
"""safe tyoing"""
from typing import Any, Sequence, Union
# The types of the elements of the input are not know


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function that does safe typing"""
    if lst:
        return lst[0]
    else:
        return None
