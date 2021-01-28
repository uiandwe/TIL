# -*- coding: utf-8 -*-
from collections import defaultdict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict(list)
        self.capacity = capacity
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.count += 1
            self.cache[key][1] = self.count
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        self.count += 1
        if key in self.cache.keys() or self.capacity > len(self.cache):
            self.cache[key] = [value, self.count]
        else:
            # history의 가장 작은 값 삭제
            d = sorted(self.cache.items(), key=lambda x: x[1][1])
            del self.cache[d[0][0]]
            self.cache[key] = [value, self.count]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
assert lRUCache.get(1) == 1
lRUCache.put(3, 3)
assert lRUCache.get(2) == -1
lRUCache.put(4, 4)
assert lRUCache.get(1) == -1
assert lRUCache.get(3) == 3
assert lRUCache.get(4) == 4

lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(2, 2)
assert lRUCache.get(2) == 2
lRUCache.put(1, 1)
lRUCache.put(4, 1)
assert lRUCache.get(2) == -1
