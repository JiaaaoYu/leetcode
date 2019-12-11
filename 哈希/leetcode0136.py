class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)
        
        return sum(hashset)*2 - sum(nums)