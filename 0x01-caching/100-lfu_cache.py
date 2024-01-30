#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class
    """

    def __init__(self):
        """ Initialize the LFUCache
        """
        super().__init__()
        self.frequency = {}
        self.time_of_last_access = {}
        self.time_counter = 0

    def put(self, key, item):
        """ Add an item in the cache using LFU algorithm
        """
        if key is not None and item is not None:
            self.time_of_last_access[key] = self.time_counter
            self.time_counter += 1

            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                keys_to_discard = [k for k, v in self.frequency.items()\
                        if v == min_frequency]

                if len(keys_to_discard) > 1:
                    lru_key = min(keys_to_discard,\
                            key=lambda x: self.time_of_last_access[x])
                    keys_to_discard.remove(lru_key)

                for discard_key in keys_to_discard:
                    del self.cache_data[discard_key]
                    del self.frequency[discard_key]
                    del self.time_of_last_access[discard_key]
                    print("DISCARD: {}".format(discard_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key and update its usage in LFU order
        """
        if key is not None and key in self.cache_data:
            self.time_of_last_access[key] = self.time_counter
            self.time_counter += 1

            self.frequency[key] += 1

            return self.cache_data[key]
        return None
