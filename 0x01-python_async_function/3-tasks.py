#!/usr/bin/python3
"""Module with function task_wait_random that
takes an integer max_delay and returns a asyncio.Task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """Returns an asyncio task without creating an asyncio function

    Args:
        max_delay (int): Maximum number of seconds to wait.

    Returns:
        float: Asyncio.Task
    """
    return (wait_random(max_delay))
