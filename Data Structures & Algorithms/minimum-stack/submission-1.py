class MinStack:
    #self.stack = None
    #self.minstack = None

    def __init__(self):
        self.stack = []
        self.minstack = [] # Monotonic minstack

    def push(self, val: int) -> None:
        self.stack.append(val)

        # if minstack is empty or smaller than current min, push val
        # else, duplicate the current minimum at the top of the minstack
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        if(self.stack):
            val = self.stack.pop()
            self.minstack.pop() # need to pop from both to maintain sync
        else:
            print("error: popping from empty stack")


    def top(self) -> int:
        if(self.stack):
            val = self.stack[-1]
            return val

    def getMin(self) -> int:
        if(self.minstack):
            return self.minstack[-1]
        
# my attempt #1 - optimal
# -- accidental slight cheating when looking up stack organizing
# -- o(n) time ; o(1) space