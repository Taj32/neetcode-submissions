class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        length = len(nums)
        print(length)
        for i in range(length):
            if(i != length - 1):
                if (nums[i] == nums[i+1]):
                    return True

        return False