from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        d = [0]*3
        for s in stones:
            d[s%3] += 1

        while d[1] >= 2 and d[2] >= 2:
            d[1] -= 1
            d[2] -= 1

        if d[0] % 2 == 1:  # Alice can pass its turn 1 more time than bob
            if (d[1] == 0 and d[2] > 2) or (d[2] == 0 and d[1] > 2):
                return True
            if (d[1] == 1 and d[2] > 3) or (d[2] == 1 and d[1] > 3):
                return True
        else:
            if (d[1] == 1 and d[2] > 0) or (d[2] == 1 and d[1] > 0):
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    assert s.stoneGameIX([2, 1])
    assert not s.stoneGameIX([2])
    assert not s.stoneGameIX([5, 1, 2, 4, 3])
    assert not s.stoneGameIX([2, 3])
