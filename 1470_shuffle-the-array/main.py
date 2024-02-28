from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = []
        for i in range(n):
            l.append(nums[i])
            l.append(nums[i+n])
        return l

if __name__ == '__main__':
    s = Solution()
    assert s.shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7]
    assert s.shuffle([1,2,3,4,4,3,2,1], 4) == [1,4,2,3,3,2,4,1]
    assert s.shuffle([1,1,2,2], 2) == [1,2,1,2]


