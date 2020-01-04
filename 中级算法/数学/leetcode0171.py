class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        bit = 1
        for a in s[::-1]:
            res += (ord(a) - ord('A') + 1) * bit
            bit *= 26
        return res
