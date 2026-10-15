from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()

        for asteroid in asteroids:
            destroyed = False

            while stack and (stack[-1] > 0 and asteroid < 0):
                if abs(asteroid) < abs(stack[-1]):
                    destroyed = True
                    break
                elif abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                else:
                    stack.pop()
                    destroyed = True
                    break

            if not destroyed:
                stack.append(asteroid)

        return stack
