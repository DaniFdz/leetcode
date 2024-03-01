from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        r = [0]*len(temperatures)
        for i,x in enumerate(temperatures):
            while s and x > temperatures[s[-1]]:
                e = s.pop()
                r[e] = i-e
            s.append(i)
        return r



if __name__ == '__main__':
    s = Solution().dailyTemperatures
    assert s([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert s([30,40,50,60]) == [1,1,1,0]
    assert s([30,60,90]) == [1,1,0]
