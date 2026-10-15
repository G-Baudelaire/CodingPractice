# Group Anagrams
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            hashmap[key].append(s)

        return list(hashmap.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution().groupAnagrams(strs)
    print(solution)
