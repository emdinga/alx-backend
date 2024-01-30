#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class
    """

    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()
        self.mru_list = []

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.mru_list.pop(0)
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))

            self.cache_data[key] = item
            self.mru_list.append(key)

    def get(self, key):
        """ Get an item by key and update its usage in MRU order
        """
        if key is not None and key in self.cache_data:
            self.mru_list.remove(key)
            self.mru_list.append(key)
            return self.cache_data[key]
        return None
