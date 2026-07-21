class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            # If opening bracket, push to stack
            if char in '({[':
                stack.append(char)
            # If closing bracket
            else:
                # Check if stack is empty (no matching opening bracket)
                if not stack:
                    return False
                
                # Check if top of stack matches
                if (char == ')' and stack[-1] == '(') or \
                   (char == '}' and stack[-1] == '{') or \
                   (char == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
        
        # Stack should be empty if all brackets matched
        return len(stack) == 0
