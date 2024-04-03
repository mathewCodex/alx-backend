#!/usr/bin/env python3
"""Basic caching mod
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Rep an obj that allows storing
    and retreiving items from a dictionary
    """
    def put(self, key, item):
        """Add an item in the
        cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retreives an item by key
        """
        return self.cache_data.get(key, None)
