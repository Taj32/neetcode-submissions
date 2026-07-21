class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        midPoint = len(nums) // 2
        left = nums[:midPoint]
        right = nums[midPoint:]

        return(min(nums))

        # while len(left) != 1 or len(right) != 1:
        #     #how to keep splicing

        #     #picking the left or right option given rotation


        if (len(left) == 1):
            return(left[0])
        else:
            return(right(0))