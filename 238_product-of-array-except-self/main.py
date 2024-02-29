from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zeros = 0

        for n in nums:
            if n != 0:
                p*=n
            else:
                zeros += 1

        if zeros > 1:
            return [0] * len(nums)

        if zeros == 1:
            return [0 if n!=0 else p for n in nums]

        return [int(p/n) for n in nums]


if __name__ == '__main__':
    s = Solution()
    assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
