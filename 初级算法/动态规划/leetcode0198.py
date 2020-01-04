class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        
        return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        pre_max, cur_max = 0, 0
        for num in nums:
            pre_max, cur_max = cur_max, max(pre_max+num, cur_max)
        
        return cur_max