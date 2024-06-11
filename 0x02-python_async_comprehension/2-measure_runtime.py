#!/usr/bin/env python3
"""Import async_comprehension from the previous file
and write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself."""
import time
import asyncio

async_com = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of 4 asynchronous function

    Return:
        returns the total time it takes to run the function asychronously
    """
    t = time.perf_counter()
    await asyncio.gather(async_com(), async_com(), async_com(), async_com())
    return time.perf_counter() - t
