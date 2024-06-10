#!/usr/bin/env python3
"""asynchronous coroutine that
takes in an integer argument """
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """Function to execute async command"""
    await asyncio.sleep(max_delay)
    return uniform(0, max_delay)
