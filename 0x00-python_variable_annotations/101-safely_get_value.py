#!/usr/bin/env python3
"""Given the parameters and the return values,
add type annotations to the function"""
from typing import Mapping, Any, Union, TypeVar

x = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[x, None] = None) -> Union[Any, x]:
    if key in dct:
        return dct[key]
    else:
        return default
