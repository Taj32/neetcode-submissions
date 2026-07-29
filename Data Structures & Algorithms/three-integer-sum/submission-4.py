class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        #1. sort the input
        nums.sort()

        #2. iterate
        for i, a in enumerate(nums):
            # Case: dont reuse the same value twice
            if(i > 0 and a == nums[i-1]):
                continue

            # 3. two pointer solution
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if(threeSum > 0):
                    r -= 1
                elif(threeSum < 0):
                    l += 1
                elif(threeSum == 0):
                    result.append([a,nums[l], nums[r]])

                    # don't reuse left and right numbers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1 

                    # move both pointers inwards (to not repeat)
                    l += 1
                    r -= 1
            
        return result
                