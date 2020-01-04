class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        
        return res

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * n for n in range(1, numRows+1)]
        for i in range(numRows):
            dp[i][0] = dp[i][-1] = 1
        for i in range(numRows):
            for j in range(i+1):
                if dp[i][j] == 0:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                    
        return dp