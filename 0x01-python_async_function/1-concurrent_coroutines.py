#!/usr/bin/env python3
"""takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values).
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: any) -> list:
    """Gets a list of delays from wait_random

    Args:
        n (int): The number of iterations
        max_delay (int): Maximum number of seconds to wait. Default is 10.

    Returns:
        float: A random float between 0 and max_delay.
    """
    result = sorted([await wait_random(max_delay) for i in range(n)])
    return result
