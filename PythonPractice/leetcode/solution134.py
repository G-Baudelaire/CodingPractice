from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        difference = [gas[i] - cost[i] for i in range(length)]

        total, current_tank = 0, 0
        result = 0
        for index in range(length):
            total += difference[index]
            current_tank += difference[index]
            if current_tank < 0:
                current_tank = 0
                result = index + 1

        return -1 if total < 0 else result
