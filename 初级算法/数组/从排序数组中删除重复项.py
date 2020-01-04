class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        idx = 0
        pre = nums[0]
        for i, num in enumerate(nums):
            if i == 0 or num != pre:
                nums[idx] = num
                pre = num
                idx += 1
        
        return idx