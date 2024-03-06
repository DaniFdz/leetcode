class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        l = m = 0
        for i, x in enumerate(s):
            if seen.get(x, -1) >= l:
                l = seen[x]+1

            m = max(m, i+1-l)
            seen[x] = i

        return m



if __name__ == '__main__':
    s = Solution().lengthOfLongestSubstring
    assert s(" ") == 1
    assert s("") == 0
    assert s("abcabcbb") == 3
    assert s("bbbbb") == 1
    assert s("pwwkew") == 3
    assert s("au") == 2
