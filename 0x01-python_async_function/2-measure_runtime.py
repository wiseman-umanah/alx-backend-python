#!/usr/bin/env python3
"""Module that creates a measure_time function
with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay),
and returns total_time / n."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the time of program execution
    
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): Maximum number of seconds to wait. Default is 10.

    Returns:
        float: Time Measurement in seconds
    """
    t = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - t) / n
