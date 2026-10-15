# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = tuple(char for char in s.lower() if char.isalnum())
        return s ==  s[::-1]


if __name__ == '__main__':
    test = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(test))
