from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm = dict()
        for n in arr:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1
        l = -1
        for k,v in hm.items():
            if k == v and k > l:
                l = k
        return l

if __name__ == '__main__':
    s = Solution()
    assert s.findLucky([2,2,3,4]) == 2
    assert s.findLucky([1,2,2,3,3,3]) == 3
    assert s.findLucky([2,2,2,3,3]) == -1
    assert s.findLucky([4,3,2,2,4,1,3,4,3]) == 3

