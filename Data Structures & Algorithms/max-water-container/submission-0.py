class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            maxArea = max(maxArea, area)
            
            # Move the pointer with smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea