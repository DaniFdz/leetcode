from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        boundCount = 0

        for n in nums:
            position += n
            boundCount += 1 if position == 0 else 0

        return boundCount


if __name__ == "__main__":
    s = Solution()
    assert s.returnToBoundaryCount([2, 3, -5]) == 1
    assert s.returnToBoundaryCount([3,2,-3,-4]) == 0
