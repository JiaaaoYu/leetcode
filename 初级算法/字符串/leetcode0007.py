class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x >= 0 else -1
        
        chars = list(str(abs(x)))
        start, end = 0, len(chars)-1
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
        
        idx = 0
        for i, item in enumerate(chars):
            if item != 0:
                idx = i
                break
        
        if int("".join(chars[idx:])) > 2**31 - 1 or int("".join(chars[idx:])) < -2*31:
            return 0
        return flag * int("".join(chars[idx:]))