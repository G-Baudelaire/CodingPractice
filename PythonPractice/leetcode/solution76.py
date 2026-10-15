class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, len(s) - 1
        self._elements = [0] * 128
        self.addToElements(t)
        self.subtractToElements(s)

        minWindowString = ""
        while left <= right and right < len(s):
            if self.isAllNegativeOrZero():
                minWindowString = s[left : right + 1]
                rightCharacter = s[right]
                self._elements[ord(rightCharacter)] += 1
                right -= 1
            else:
                self._elements[ord(s[left])] += 1
                left += 1
                right += 1
                if right < len(s):
                    self._elements[ord(s[right])] -= 1
        return minWindowString

    def addToElements(self, string: str):
        for char in string:
            self._elements[ord(char)] += 1

    def subtractToElements(self, string: str):
        for char in string:
            self._elements[ord(char)] -= 1

    def isAllNegativeOrZero(self):
        return all(map(lambda count: count <= 0, self._elements))
