class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        index = 0
        for c in s:
            if count[c] == 1:
                return index
            else:
                index += 1
        
        return -1