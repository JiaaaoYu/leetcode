class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        pre, res = 0, 0
        for c in reversed(s):
            tmp = mapping.get(c)
            if tmp < pre:
                res -= tmp
            else:
                res += tmp
                pre = tmp
                
        return res
        