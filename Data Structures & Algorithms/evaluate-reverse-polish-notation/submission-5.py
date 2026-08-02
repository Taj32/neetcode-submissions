class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for token in tokens:
            if token in ops:
                b = stack.pop()   # right operand — pushed most recently
                a = stack.pop()   # left operand — pushed before that
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))   # truncate toward zero, every time
            else:
                stack.append(int(token))

        return stack[-1]
# ollama solution --> O(n) time, O(n) space