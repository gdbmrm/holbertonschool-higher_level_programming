#!/usr/bin/python3

class CountedIterator():
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0

    def __next__(self):
        try:
            self.count += 1
            prochain = next(self.iterator)
            return prochain
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count
