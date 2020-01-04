class Solution:
    def isValid(self, s: str) -> bool:
        stack, pair = [], {"(": ")", "{": "}", "[": "]"}
        for item in s:
            if item in pair:
                stack.append(item)
            else:
                if len(stack) == 0 or pair[stack.pop()] != item:
                    return False
                
        return len(stack) == 0