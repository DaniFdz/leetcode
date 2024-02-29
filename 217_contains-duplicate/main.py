from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)

        return False

if __name__ == '__main__':
    s = Solution()
    assert s.containsDuplicate([1,2,3,1])
    assert not s.containsDuplicate([1,2,3,4])
    assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
