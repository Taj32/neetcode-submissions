class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ollama solution
        seen = {}  # value -> index
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        
        return []