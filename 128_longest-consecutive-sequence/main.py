from typing import Dict, List, Set


class Solution:
    nums: Set[int]

    def __getCount(self, n: int, mem: Dict[int, int]) -> int:
        x = mem.get(n, -1)
        if x != -1:
            return x
        x = 0
        if n in self.nums: x = self.__getCount(n-1, mem) + 1
        mem[n] = x
        return x

    def longestConsecutive(self, nums: List[int]) -> int:
        self.nums = set(nums)
        m = 0
        mem: Dict[int, int] = dict()
        for n in nums:
            x = self.__getCount(n, mem)
            m = max(m, x)
        return m


if __name__ == '__main__':
    s = Solution().longestConsecutive
    assert s([100,4,200,1,3,2]) == 4
    assert s([0,3,7,2,5,8,4,6,0,1]) == 9
