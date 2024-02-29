from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(s)):
            d1[s[i]] += 1
            d2[t[i]] += 1

        if len(d1.keys()) != len(d2.keys()):
            return False

        for k,v in d1.items():
            if v != d2[k]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isAnagram("anagram", "nagaram")
    assert not s.isAnagram("rat", "car")
