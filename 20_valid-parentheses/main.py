class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        v = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in v:
                q.append(c)
            else:
                if q.__len__() == 0 or v[q[-1]] != c:
                    return False
                q.pop()

        return q.__len__() == 0


if __name__ == "__main__":
    s = Solution().isValid
    assert s("()")
    assert s("()[]{}")
    assert not s("(]")
    assert not s("[")
    assert not s("]")
