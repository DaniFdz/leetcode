from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = Counter(nums)
        o = sorted(f.items(), key=lambda x: x[1], reverse=True)[:k]
        return list([x[0] for x in o])



if __name__ == "__main__":
    s = Solution()
    assert s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
    assert s.topKFrequent(nums = [1], k = 1) == [1]
