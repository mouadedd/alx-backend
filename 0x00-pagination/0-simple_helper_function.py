#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """a fast way to test the checker"""
    l_index = 0

    for i in range(page):
        f_index = l_index
        l_index += page_size
    return(f_index, l_index)
