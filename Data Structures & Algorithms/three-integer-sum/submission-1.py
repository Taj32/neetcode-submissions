from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Defend against empty or too-small arrays
        if not nums or len(nums) < 3:
            return []
            
        # 1. Sort the array (Crucial for the two-pointer approach)
        nums.sort()
        triplets = []
        n = len(nums)
        
        # 2. Iterate through the array
        for i in range(n - 2):
            # If the current number is greater than 0, three positive numbers 
            # can never sum to 0. Stop looking entirely.
            if nums[i] > 0:
                break
                
            # SKIP DUPLICATES for the first element: 
            # If this number is the same as the previous one, skip it to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 3. Two Pointers initialization (always start ahead of i)
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # SKIP DUPLICATES for the second element (left pointer)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # SKIP DUPLICATES for the third element (right pointer)
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers inward after finding a match
                    left += 1
                    right -= 1
                    
                elif total < 0:
                    # Sum is too small, make it larger by moving the left pointer rightward
                    left += 1
                else:
                    # Sum is too big, make it smaller by moving the right pointer leftward
                    right -= 1
                    
        return triplets

# ollama solution
# complexity; o(n^2) ; o(1)