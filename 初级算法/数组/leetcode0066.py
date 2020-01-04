class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for i in digits[::-1]:
            tmp = (carry + i)%10
            carry = (carry + i)//10
            res.append(tmp)
        if carry != 0:
            res.append(carry)
            
        return res[::-1]