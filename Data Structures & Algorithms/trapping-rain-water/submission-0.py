class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while(l < r):
            if leftMax < rightMax:
                #increment left pointer
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] # does not need negative check because leftMax set first
            else:
                #increment right pointer
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            
        return res


# neetcode solution:
# O(n) time, o(1) space
# left, right pointer approach

# 1) set variables
# 2) Loop:
# 3) move pointer with smaller max

# 1) set new maxLeft/maxRight with new pointer pointer
# 2) shift pointer with smaller maxHeight
# 3) calculate height: maxLeft/maxright - height[i]