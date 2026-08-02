class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p , s] for p, s in zip(position, speed)]
        
        stack = []
        # traversing in reverse order approach
        # if there is a fleet forming we essentially pop out the current element
        # remember: fleet = lengeth of the stack in this scenario

        for p,s in sorted(pair)[::-1]: #reversed sorted order
            time = (target - p) / s 
            stack.append((target - p) / s )

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

# video solutions