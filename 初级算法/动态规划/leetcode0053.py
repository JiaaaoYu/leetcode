class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, mx = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], nums[i]+cur)
            mx = max(mx, cur)
        
        return mx


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
            