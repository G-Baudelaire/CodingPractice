from heapq import heapify, heapreplace


class SmallestInfiniteSet:
    def __init__(self):
        self.missing = set()

    def popSmallest(self) -> int:
        smallest = 1
        while True:
            if smallest not in self.missing:
                self.missing.add(smallest)
                return smallest
            smallest += 1

    def addBack(self, num: int) -> None:
        if num in self.missing:
            self.missing.remove(num)