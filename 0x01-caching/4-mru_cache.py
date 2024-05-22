#!/usr/bin/env python3
"""4.MRU caching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """initialize the class"""
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """ put cache and manage it with MRU"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and\
                    key not in self.cache_data:
                print(f"DISCARD: {self.cache_list[-1]}")
                del self.cache_data[self.cache_list[-1]]
                del self.cache_list[-1]
            if key in self.cache_list:
                del self.cache_list[self.cache_list.index(key)]
            self.cache_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            del self.cache_list[self.cache_list.index(key)]
            self.cache_list.append(key)
            return self.cache_data[key]
