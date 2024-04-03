#!/usr/bin/env python3
"""First-In First-Out caching
      mod
"""
from collection import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Rep an obj that allows storing
    retreiving items from a dict with a FIFO
    removal mechanism when the limit is reached
    """
    def __init__(self):
        """Init the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key
        """
        return self.cache_data.get(key, None)
