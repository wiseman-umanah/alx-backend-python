#!/usr/bin/env python3
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    result = sorted([await wait_random(max_delay) for i in range(n)])
    return result
