from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude, max_altitude = 0, 0
        for num in gain:
            altitude += num
            max_altitude = max(max_altitude, altitude)
        return max_altitude