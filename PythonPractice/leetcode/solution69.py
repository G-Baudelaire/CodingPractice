class IterativeMathematicalSolution:
    def mySqrt(self, x: int) -> int:
        prev_estimate = float("inf")
        current_estimate = x
        while abs(prev_estimate - current_estimate) > 0.01:
            current_estimate, prev_estimate = (
                0.5 * (current_estimate + x / current_estimate),
                current_estimate,
            )
        return int(current_estimate)


# Binary Search Solution
class BinarySearchSolution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x

        lower_bound = 1
        upper_bound = x
        while upper_bound - lower_bound != 1:
            middle_point = int((upper_bound + lower_bound) / 2)
            middle_point_squared = middle_point**2

            if middle_point_squared == x:
                return middle_point
            elif middle_point_squared < x:
                lower_bound = middle_point
            else:
                upper_bound = middle_point

        return lower_bound


# Binary Search Solution
class Solution:
    def mySqrt(self, x: int) -> int:
        upper_bound = self.get_upper_bound(x)
        lower_bound = 0
        while lower_bound < upper_bound:
            print(lower_bound, upper_bound)
            queried_root = (upper_bound + lower_bound) // 2
            squared_query = queried_root * queried_root
            if squared_query == x:
                lower_bound = upper_bound = queried_root
            elif squared_query < x:
                lower_bound = queried_root
            else:
                upper_bound = queried_root
        return lower_bound

    def get_upper_bound(self, x):
        power_of_two = 0
        while x != 0:
            x >>= 1
            power_of_two += 1
        return 1 << power_of_two


test = 8
print(Solution().mySqrt(test))
