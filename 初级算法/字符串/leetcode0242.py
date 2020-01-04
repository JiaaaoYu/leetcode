class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = collections.defaultdict(int)
        for c in s:
            lookup[c] += 1
        
        for c in t:
            if c not in lookup:
                return False
            lookup[c] -= 1
        
        for c in lookup:
            if lookup[c] != 0:
                return False
        
        return True