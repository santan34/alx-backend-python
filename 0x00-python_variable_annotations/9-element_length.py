#!/usr/bin/env python3
"""more complex typing"""
from typing import Iterable, Sequence, Tuple
import typing


def element_length(lst: Iterable[Sequence]
                   ) -> typing.List[Tuple[Sequence, int]]:
    """element length"""
    return [(i, len(i)) for i in lst]
