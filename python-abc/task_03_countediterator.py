#!/usr/bin/env python3
"""
module counted iterator
"""


class CountedIterator():
    def __init__(self, some_iterable):
        """
        constructor
        """
        self.iterator = iter(some_iterable)
        self.count = 0

    def __next__(self):
        """
        method next
        """
        try:
            prochain = next(self.iterator)
            self.count += 1
            return prochain
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        return the count
        """
        return self.count
