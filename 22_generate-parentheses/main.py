from typing import List


class Solution:
    max_depth: int
    def __gen(self, current: str, open: int, close: int) -> List[str]:
        x = []
        if close == self.max_depth:
            return [current]
        if open < self.max_depth:
            for s in self.__gen(current+"(", open+1, close):
                x.append(s)
        if close < open:
            for s in self.__gen(current+")", open, close+1):
                x.append(s)
        return x

    def generateParenthesis(self, n: int) -> List[str]:
        self.max_depth = n
        return self.__gen("", 0, 0)


if __name__ == '__main__':
    s = Solution().generateParenthesis
    assert s(3) == ["((()))","(()())","(())()","()(())","()()()"]
    assert s(1) == ["()"]
