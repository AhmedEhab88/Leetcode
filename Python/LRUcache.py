class LRUCache:
    cache = dict()
    values = []
    time = 0
    capacity = 0

    def __init__(self, capacity: int):
        self.values = [None] * capacity
        self.cache = dict.fromkeys((range(capacity)))
        self.time = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.time += 1
            self.cache[key] = self.time
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if len(self.cache) != self.capacity:
            self.cache[key] = self.time
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
