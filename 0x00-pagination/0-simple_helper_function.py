#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    if page == 1:
        return(0, page_size*page)
    return(page * 10, page_size * page)
