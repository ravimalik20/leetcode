class LRUCache:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__cache = dict()

        self.__order = []

    def get(self, key: int) -> int:
        if key not in self.__cache:
            return -1

        val = self.__cache[key]
        self.__update_location(key)

        return val

    def put(self, key: int, value: int) -> None:
        self.__cache[key] = value

        self.__update_location(key)

        if len(self.__cache.keys()) > self.__capacity:
            self.__evict_lru()

    def __update_location(self, key: int):
        if key in self.__order:
            self.__order.pop(self.__order.index(key))
        self.__order.append(key)

    def __evict_lru(self):
        key = self.__order.pop(0)

        del (self.__cache[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)