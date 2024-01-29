#!/usr/bin/env python3
"""
index_range
"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of start and end indexes for pagination."""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
