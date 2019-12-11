class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicts = collections.defaultdict(int)
        res = []
        for i in nums1:
            dicts[i] += 1
            
        for i in nums2:
            if dicts[i] != 0:
                res.append(i)
                dicts[i] -= 1
                
        return res