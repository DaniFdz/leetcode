from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f = s = 0
        for n in nums:
            if n > f:
                f,s = n,f
            elif n > s:
                s = n

        return (f-1)*(s-1)


if __name__ == '__main__':
    s = Solution()
    assert s.maxProduct([3,4,5,2]) == 12
    assert s.maxProduct([1,5,4,5]) == 16
    assert s.maxProduct([3,7]) == 12
