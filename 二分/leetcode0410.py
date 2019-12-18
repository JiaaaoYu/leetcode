class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(nums, m, s):
            cnt, cur_sum = 1, 0
            for num in nums:
                cur_sum += num
                if cur_sum > s:
                    cur_sum = num
                    cnt += 1
                    
            return cnt <= m
        
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if canSplit(nums, m, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    