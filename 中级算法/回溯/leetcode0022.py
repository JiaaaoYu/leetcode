class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(com="", left=0, right=0):
            if len(com) == 2*n:
                res.append(com)
                return 
            if left < n:
                backtrack(com+'(', left+1, right)
            if right < left:
                backtrack(com+')', left, right+1)
            
        backtrack()
        return res
            