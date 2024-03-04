from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

        return [-1, -1]


if __name__ == "__main__":
    s = Solution().twoSum
    assert s(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert s(numbers=[2, 3, 4], target=6) == [1, 3]
    assert s(numbers=[-1, 0], target=-1) == [1, 2]
