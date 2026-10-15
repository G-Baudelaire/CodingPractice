# Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        previous_values = {}

        for integer in self.iteration(n):
            if integer == 1:
                return True
            elif integer in previous_values:
                return False
            else:
                previous_values[integer] = True

    def iteration(self, n):
        while True:
            digits = list()

            while n > 0:
                digits.append(n % 10)
                n //= 10
            n = sum(map(lambda x: x ** 2, digits))
            yield n


if __name__ == '__main__':
    gen = Solution().iteration(19)
    for i in range(10):
        print(gen.__next__())
