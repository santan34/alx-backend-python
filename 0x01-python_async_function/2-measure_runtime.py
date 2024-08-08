#!/usr/bin/env Python3
"""time.perf_counter"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the runtime"""
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_elapsed: float = time.perf_counter() - start
    return time_elapsed / n
