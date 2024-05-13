from collections import defaultdict
from typing import List


class Solution:

    def longestCycle(self, edges: List[int]) -> int:
        memo = defaultdict(int)
        for i in range(len(edges)):
            j = i
            visited = {i}
            v = [i]
            while edges[j] != -1:
                j = edges[j]
                if j in visited:
                    found = -1
                    for index, val in enumerate(v):
                        if val == j:
                            found = index
                        if found != -1:
                            memo[val] = len(v) - found
                    break

                visited.add(j)
                v.append(j)
        return -1 if len(memo) == 0 else max(*memo.values())



if __name__ == "__main__":
    assert Solution().longestCycle([3, 3, 4, 2, 3]) == 3
    assert Solution().longestCycle([2, -1, 3, 1]) == -1
