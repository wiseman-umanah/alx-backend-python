#!/usr/bin/env python3
"""asynchronous coroutine that
takes in an integer argument """
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Pause for max_delay seconds and
    return a random float between 0 and max_delay.

    Args:
        max_delay (int): Maximum number of seconds to wait.
        Default is 10.

    Returns:
        float: A random float between 0 and max_delay.
    """
    await asyncio.sleep(max_delay)
    return uniform(0, max_delay)
