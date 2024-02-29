from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = dict()
        for i, n in enumerate(nums):
            if n in remaining:
                return [remaining[n], i]
            remaining[target-n] = i

        return [-1,-1]

if __name__ == '__main__':
    s = Solution()
    assert s.twoSum(nums = [2,7,11,15], target = 9) == [0, 1]
    assert s.twoSum(nums = [3,2,4], target = 6) == [1, 2]
    assert s.twoSum(nums = [3,3], target = 6) == [0, 1]
