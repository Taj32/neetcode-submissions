class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []


    def push(self, val: int) -> None:
        self.stack.append(val)

        # for second stack
        # if there is already a value inserted in minstack take the min(val, currentmin)
        # and push that on top of the minstack
        val = min(val, self.minstack[-1] if self.minstack else val) #  self.minstack[-1] if self.minstack val --> take the top of min if its not empty, if it is empty just default to val
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop() # need to keep the stacks in sync

    def top(self) -> int:
        return self.stack[-1] # we dont have to worry about empty edge case because of constraints
        

    def getMin(self) -> int:
        return self.minstack[-1]

#video solution