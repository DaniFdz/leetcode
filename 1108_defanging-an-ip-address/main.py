class Solution:
    def defangIPaddr(self, address: str) -> str:
       return address.replace('.', '[.]')

if __name__ == '__main__':
    s = Solution()
    assert s.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert s.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
