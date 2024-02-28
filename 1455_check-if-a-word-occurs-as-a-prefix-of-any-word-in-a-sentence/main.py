class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(' ')):
            if word.startswith(searchWord):
                return i + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.isPrefixOfWord("i love eating burger", "burg") == 4
    assert s.isPrefixOfWord("this problem is an easy problem", "pro") == 2
    assert s.isPrefixOfWord("i am tired", "you") == -1

