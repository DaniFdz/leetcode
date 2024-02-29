from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strs:
            a = "".join(sorted(w))
            d[a].append(w)

        return list([v for v in d.values()])


if __name__ == '__main__':
    def sort_list(strs: List[List[str]]) -> List[List[str]]:
        return sorted([sorted(s) for s in strs])

    def assert_almost_equal(strs1: List[str], strs2: List[List[str]]) -> None:
        expected = sort_list(strs2)
        result = sort_list(Solution().groupAnagrams(strs1))
        assert result == expected

    assert_almost_equal(["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]])
    assert_almost_equal([""], [[""]])
    assert_almost_equal(["a"], [["a"]])

