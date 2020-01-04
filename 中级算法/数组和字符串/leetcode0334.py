class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_first, min_second = float('inf'), float('inf')
        for num in nums:
            min_first = min(min_first, num)
            if num > min_first:
                min_second = min(min_second, num)
            if num > min_second:
                return True
            
        return False