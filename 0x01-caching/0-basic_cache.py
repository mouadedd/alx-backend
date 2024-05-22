#!/usr/bin/env python3
"""0. Basic dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
 
    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
