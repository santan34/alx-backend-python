#!/usr/bin/env python3
"""concurrent coroutines"""

import asyncio
import random
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    spawn_list: List[float]= []
    return_list: List[float]= []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        spawn_list.append(task)

    delays = await asyncio.gather(*spawn_list)
    
    return sorted(delays)gi
