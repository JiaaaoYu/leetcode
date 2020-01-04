class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # return n > 0 and n == 3**(round(math.log(n, 3)))
        if n <= 0:
            return False
        while True:
            if n%3==0:
                n//=3
            elif n==1:
                return True
            else:
                return False
