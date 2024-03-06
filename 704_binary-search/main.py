from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (r - l) // 2 + l
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return -1

if __name__ == "__main__":
    s = Solution().search
    assert s(nums = [-1,0,3,5,9,12], target = 9) == 4
    assert s(nums = [-1,0,3,5,9,12], target = 2) == -1
    assert s(nums = [1], target = 1) == 0
