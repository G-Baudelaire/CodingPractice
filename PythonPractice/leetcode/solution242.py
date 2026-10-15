# Valid Anagram
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)

        for char in s:
            hashmap[char] += 1

        for char in t:
            hashmap[char] -= 1

        return all(value==0 for value in hashmap.values())

    def get_hashmap(self, string_set, string):
        hashmap = {key: 0 for key in string_set}
        for char in string:
            hashmap[char] += 1
        return hashmap

    def quick_to_implement_is_anagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
