from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = max(0, capacity)
        self.store = OrderedDict()

    def get(self, key):
        if key not in self.store:
            return -1
        value = self.store.pop(key)
        self.store[key] = value  # mark as recently used
        return value

    def set(self, key, value):
        if self.capacity == 0:
            return
        if key in self.store:
            self.store.pop(key)
        elif len(self.store) >= self.capacity:
            self.store.popitem(last=False)
        self.store[key] = value


if __name__ == "__main__":
    cache = LRU_Cache(5)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    print(cache.get(1))  # 1
    print(cache.get(2))  # 2
    print(cache.get(9))  # -1
    cache.set(5, 5)
    cache.set(6, 6)  # evicts key 3
    print(cache.get(3))  # -1

    # Edge: capacity 0
    empty_cache = LRU_Cache(0)
    empty_cache.set(1, 10)
    print(empty_cache.get(1))  # -1

    # Edge: overwrite existing key
    cache.set(2, 20)
    print(cache.get(2))  # 20
