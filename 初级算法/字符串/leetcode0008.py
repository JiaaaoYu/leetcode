class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        res = 0
        i = 0
        n = len(str)
        sign = 1
        max_num = 2**31-1
        min_num = -2**31
        if i < n :
            if str[i] == "-":
                sign = -1
                i += 1
            elif str[i] == "+":
                i += 1    
        while i < n and str[i].isdigit():
            #print(res)
            res = 10 * res + int(str[i])
            if res > max_num or res < min_num:
                if sign == 1:
                    return max_num
                else:
                    return min_num    
            i += 1
        return res * sign
