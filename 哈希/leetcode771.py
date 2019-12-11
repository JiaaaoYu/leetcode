class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        all_set = set(J)
        res = 0
        for s in S:
            if s in all_set:
                res += 1
        
        return res