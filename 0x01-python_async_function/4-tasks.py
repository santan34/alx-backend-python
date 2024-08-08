#!/usr/bin/env python3
"""concurrent coroutines"""

import asyncio
import random
from typing import List, Set, Any
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """asynchronous handling """
    task_list: Set[Any] = set()
    for i in range(n):
        task = task_wait_random(max_delay)

        task_list.add(task)

    list: List[float] = await asyncio.gather(*task_list)
    return list
