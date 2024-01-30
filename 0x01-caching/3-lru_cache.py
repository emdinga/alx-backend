#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache class
    """

    def __init__(self):
        """ Initialize the LRUCache
        """
        super().__init__()
        self.order_dict = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.order_dict.popitem(last=False)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

            self.cache_data[key] = item
            self.order_dict[key] = True

    def get(self, key):
        """ Get an item by key and update its usage in LRU order
        """
        if key is not None and key in self.cache_data:
            self.order_dict.pop(key)
            self.order_dict[key] = True
            return self.cache_data[key]
        return None
