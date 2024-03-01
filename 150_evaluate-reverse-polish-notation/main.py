from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if len(t) == 1 and ord(t) < 48:
                n2 = s.pop()
                n1 = s.pop()
                match t:
                    case "+":
                        t = n1 + n2
                    case "-":
                        t = n1 - n2
                    case "*":
                        t = n1 * n2
                    case "/":
                        t = n1 / n2

            s.append(int(t))

        return s.pop()


if __name__ == "__main__":
    s = Solution().evalRPN
    assert s(["2", "1", "+", "3", "*"]) == 9
    assert s(["4", "13", "5", "/", "+"]) == 6
    assert s(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
