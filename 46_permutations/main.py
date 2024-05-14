from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums[:]]
        sol = []
        for i, n in enumerate(nums):
            for p in self.permute(nums[:i] + nums[i+1:]):
                p.append(n)
                sol.append(p)
        return sol


if __name__ == "__main__":
    assert sorted(Solution().permute([1])) == sorted([[1]])
    assert sorted(Solution().permute([1, 2])) == sorted([[2, 1], [1, 2]])
    assert sorted(Solution().permute([1, 2, 3])) == sorted(
        [[2, 3, 1], [3, 1, 2], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 2, 3]]
    )
