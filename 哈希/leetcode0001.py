class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, item in enumerate(nums):
            if hashmap.get(target - item) is not None:
                return [hashmap.get(target-item), i]
            
            hashmap[item] = i