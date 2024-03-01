from typing import List
from collections import deque


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(sorted(zip(position, speed), reverse=True))
        stack = []
        for p, s in pairs:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)



if __name__ == '__main__':
    s = Solution().carFleet
    assert s(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) == 3
    assert s(target = 10, position = [3], speed = [3]) == 1
    assert s(target = 100, position = [0,2,4], speed = [4,2,1]) == 1
