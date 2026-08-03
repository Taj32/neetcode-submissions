class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 0. variables
        left = 0
        right = len(nums) - 1

        # 1. loop
        while left <= right: # looping until we find it or the array is no longer valid
            midpoint = ( right + (right - left) ) // 2

            if(nums[midpoint] == target):
                return midpoint
            elif(nums[midpoint] < target):
                # move the left pointer
                left = midpoint + 1
            else:
                # move the right pointer
                # target is towards the left side of the boundaries
                right = midpoint - 1

        return -1