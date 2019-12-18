class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        abs_n =abs(n)
        while abs_n:
            if abs_n & 1:
                result *= x
            abs_n = abs_n >> 1
            x *= x
            
        return 1/result if n < 0 else result
    