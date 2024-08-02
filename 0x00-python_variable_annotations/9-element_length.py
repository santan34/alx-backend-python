#!/usr/bin/env python3
from typing import Iterable, Sequence, Tuple
import typing


def element_length(lst: Iterable[Sequence]
                   ) -> typing.List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
