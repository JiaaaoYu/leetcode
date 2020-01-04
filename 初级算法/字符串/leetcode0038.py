class Solution:
    def countAndSay(self, n: int) -> str:
        def next(val):
            res, i = '', 0
            n = len(val)
            while i < n:
                count = 1
                while i < n - 1 and val[i] == val[i+1]:
                    count += 1
                    i += 1
                res += (str(count) + str(val[i]))
                i += 1
            return res
        
        res = "1"
        for i in range(1, n):
            res = next(res)
        return res