from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        
        # buckets[i] = list of numbers that appear exactly i times
        buckets = [[] for _ in range(n + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        # walk from highest possible frequency down to 1
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result

# Optimal solution: O(N) {length of the array}
# instead of sorting by frequency make buckets indexed by frequency (o to n)
# then drop each number into the buckets representing the count
# then walk the buckets from highest frequency down, collecting numbers until you have k