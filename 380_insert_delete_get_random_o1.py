import random

from collections import OrderedDict


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.__data = OrderedDict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.__data:
            return False

        self.__data[val] = True
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.__data:
            return False

        del (self.__data[val])
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return random.choice(list(self.__data.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()