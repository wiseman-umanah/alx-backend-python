#!/usr/bin/env python3
"""takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values).
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Function to execute the code"""
    result = sorted([await wait_random(max_delay) for i in range(n)])
    return result
