from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        l = []
        for n in nums:
            sum += n
            l.append(sum)
        return l


if __name__ == '__main__':
    s = Solution()
    assert s.runningSum([1,2,3,4]) == [1,3,6,10]
    assert s.runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert s.runningSum([3,1,2,10,1]) == [3,4,6,16,17]
