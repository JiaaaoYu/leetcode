class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if self.possible(nums, mid, k):
                high = mid
            else:
                low = mid + 1
        
        return low
        
    def possible(self, nums, guess, k):
        count = left = 0
        for idx, item in enumerate(nums):
            while item - nums[left] > guess:
                left += 1
            count += idx - left
        return count >= k
    