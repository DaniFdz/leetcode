from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        h, w = len(matrix), len(matrix[0])
        l, r = 0, w*h
        while l < r:
            m = (r - l) // 2 + l
            x, y = m // w, m % w
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                l = m + 1
            else:
                r = m

        return False

if __name__ == '__main__':
    s = Solution().searchMatrix
    assert s(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
    assert not s(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
    assert not s(matrix = [[1,1]], target=2)
    assert s(matrix = [[1],[3]], target=3)
    assert not s(matrix = [[1]], target=2)
    assert not s(matrix = [], target=0)
