#!/usr/bin/env python3
"""concurrent coroutines"""

import asyncio
import random
from typing import List, Set, Any
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """asynchronous handling """
    task_list: Set[Any] = set()
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))

        task_list.add(task)

    list: List[float] = await asyncio.gather(*task_list)
    return list
