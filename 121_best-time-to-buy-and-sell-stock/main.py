from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = int(1e4)
        m = 0
        for r in prices:
            if r < l:
                l = r
            elif r - l > m:
                m = r - l

        return m

if __name__ == '__main__':
    s = Solution().maxProfit
    assert s([7,1,5,3,6,4]) == 5
    assert s([7,6,4,3,1]) == 0
