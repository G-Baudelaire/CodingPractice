class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        function = dict()
        for s_char, t_char in zip(s, t):
            output_char = function.get(s_char)
            if output_char is not None and output_char != t_char:
                return False
            else:
                function.update({s_char: t_char})

        return len(function.keys()) == len(set(function.values()))

if __name__ == '__main__':
    s = "egg"
    t = "add"
    print(Solution().isIsomorphic(s, t))
    s = "foo"
    t = "bar"
    print(Solution().isIsomorphic(s, t))
