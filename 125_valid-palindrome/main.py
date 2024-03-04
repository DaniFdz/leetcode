class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(x.lower() for x in s if x.isalnum())
        return a == a[::-1]

if __name__ == '__main__':
    s = Solution().isPalindrome
    assert s("A man, a plan, a canal: Panama")
    assert not s("race a car")
    assert s(" ")
    assert s(".,")
    assert not s("0P")
