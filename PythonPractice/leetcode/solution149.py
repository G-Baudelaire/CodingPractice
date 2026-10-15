import itertools


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) in (1, 2):
            return len(points)

        points = (tuple(point) for point in points)
        line_counts = dict()
        for p1, p2 in itertools.combinations(points, 2):
            line = self.get_gradient_and_intercept(p1, p2)
            try:
                line_counts[line].update((p1, p2))
            except KeyError:
                line_counts[line] = {p1, p2}
            print(line_counts)

        return max(len(value) for value in line_counts.values())

    def get_gradient_and_intercept(self, p1, p2):
        y_diff = p1[1] - p2[1]
        x_diff = p1[0] - p2[0]
        gradient = float("inf") if x_diff == 0 else y_diff / x_diff
        intercept = p1[0] if x_diff == 0 else p1[1] - gradient * p1[0]
        return (gradient, intercept)


points = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
print(Solution().maxPoints(points))
