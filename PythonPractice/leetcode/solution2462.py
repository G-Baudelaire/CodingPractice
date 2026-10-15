from typing import List
from heapq import heappop, heappush


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap, right_heap = [], []
        left_pointer, right_pointer = 0, len(costs) - 1
        total_cost = 0

        for i in range(k):
            while left_pointer <= right_pointer and len(left_heap) < candidates:
                heappush(left_heap, costs[left_pointer])
                left_pointer += 1

            while left_pointer <= right_pointer and len(right_heap) < candidates:
                heappush(right_heap, costs[right_pointer])
                right_pointer -= 1
            print(left_heap, right_heap)

            if left_heap and right_heap:
                total_cost += heappop(left_heap) if left_heap[0] <= right_heap[0] else heappop(left_heap)
            elif left_heap:
                total_cost += heappop(left_heap)
            else:
                total_cost += heappop(right_heap)

        return total_cost