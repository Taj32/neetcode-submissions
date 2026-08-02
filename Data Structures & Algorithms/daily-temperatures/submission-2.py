class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # pair
        # stack[-1][0] --> temperature ; stack[-1][1] index

        # begin the loop
        for i, t in enumerate(temperatures):
            print(i)
            # check if the stack is nonempty and the current temperature of i is greater than the top of the stack
            while(stack and t > stack[-1][0]):
                # if this is the case we are going to remove from the stack and change the result
                # this is because i is the next warmest day from stackIndex
                stackTemp = stack[-1][0]
                stackIndex = stack[-1][1]

                res[stackIndex] = i - stackIndex

                #pop
                stack.pop()


            # regardless append the stack with the new pair
            stack.append([t, i])

        return res

# My attempt # 2