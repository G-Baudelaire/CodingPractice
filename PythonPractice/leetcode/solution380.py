# Insert Delete GetRandom O(1)
import random


class RandomizedSet:

    def __init__(self):
        self.hashmap = dict()
        self.list = list()

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False

        self.hashmap[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False

        # Move swap val with end of list value, then remove val.
        end_value = self.list[-1]
        val_index = self.hashmap[val]

        self.hashmap[end_value] = val_index
        self.list[val_index], self.list[-1] = self.list[-1], val

        self.list.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
