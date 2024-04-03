#!/usr/bin/env python3
"""Last-In First-Out caching mod
"""
from collections import OrderedDict

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """Rep an obj that alows storing
    and getting items from a dict
    with LIFO removal mechanism when lim
    is reached"""
    def __init__(self):
        """init the cache"""
        super().__init__()
        self.cache_data = OrderedDict()
        
    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """get an item by key"""
        return self.cache_data.get(key, None)
