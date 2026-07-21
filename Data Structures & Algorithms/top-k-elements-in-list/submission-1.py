import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # example: nums = [1,1,1,2,2,3] ; k = 2
        count = Counter(nums)
        heap = []
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap) # drop the smallest frequency
        
        # heap after pop = [(2, 2), (3, 1)]
        return [num for freq, num in heap]

# claude solution 1: o(n log k)
# only hold k elements, the k largest frequencies so far
# push each (frequency, num) pair. if the heap grows past size k pop the smallest
# at the end, whatever is left in the heap is the answer.