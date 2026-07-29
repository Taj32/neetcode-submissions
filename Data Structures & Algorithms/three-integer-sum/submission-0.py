class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if nums is None:
            return None

        # 1. sort the array
        nums.sort()
        triplets = []
        print(nums)



        # 2. Iterate over the array (until mid point)
        for index, num in enumerate(nums):
            l = 0
            r = len(nums) - 1
            while l < r: #step 3
                if(l == r or r == index or l == index):
                    l += 1
                    continue
                if( (-(nums[l]) + -(nums[r])) == (nums[index]) ):
                    # 3. triplet detected

                    temp = [nums[index], nums[l], nums[r]]
                    temp.sort()

                    if(temp in triplets):
                        l += 1
                        continue
                    else:
                        #add the distinct triplet
                        print("l = " + str(nums[l]) + ", r = " + str(nums[r]) + ", index = " + str(nums[index]))
                        triplets.append(temp)
                        l += 1
                elif( (nums[l] + nums[r]) > -(nums[index])):
                    # reduce r
                    r -= 1
                elif( (nums[l] + nums[r]) < -(nums[index])):
                    # increase l
                    l += 1
        
        # 4. return results
        return triplets
