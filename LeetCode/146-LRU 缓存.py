"""
OrderedDict
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)

        while len(self.cache) > self.capacity:
            self.cache.popitem(last=False)



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key not in self.queue:
            return -1
        
        self.__move(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.queue:
            self.__update(key, value)
        else:
            self.__add(key, value)
        
        while len(self.queue) > self.capacity:
            self.queue.pop(0)
    
    def __update(self, key, value):
        self.__move(key)
        self.cache[key] = value

    def __add(self, key, value):
        self.queue.append(key)
        self.cache[key] = value

    def __move(self, key):
        self.queue.remove(key)
        self.queue.append(key)
