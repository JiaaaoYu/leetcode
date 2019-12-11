from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = Counter(nums)
        heap = []
        for k1, v in lookup.items():
            heapq.heappush(heap, [-v, k1])
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
    

