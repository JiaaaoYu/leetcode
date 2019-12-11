class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        target = nums[-1]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                right = mid
            else:
                left = mid + 1
            
        return nums[left]
        