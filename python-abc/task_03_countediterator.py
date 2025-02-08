#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.counter = 0
        self.iterator = iter(iterable)

    def get_count(self):
        return self.counter
    
    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate.")
        
    def __iter__(self):
        return self
    