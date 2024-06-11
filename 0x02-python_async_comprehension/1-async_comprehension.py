#!/usr/bin/env python3
"""Module of a coroutine called async_comprehension
that takes no arguments.

The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers."""
from typing import List

async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The Function to implement the logic

    Return:
        List[float]: returns a list of randomly generated numbers"""
    return [i async for i in async_gen()]
