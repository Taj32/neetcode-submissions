class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # is our stack populated AND is the element at the top of the stack < currentTemp
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex) # difference = number of days till the warmer weather
            stack.append([t, i])
        # return the resulting array
        return res

# video solution: O(n) time ; O(n) space