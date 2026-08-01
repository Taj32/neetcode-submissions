class Solution:
    def isValid(self, s: str) -> bool:
        # bracket edge case:
        if(len(s) == 1):
            return False

        # 1. setup variables
        stack = []

        close_open_relationships = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        # iterate over the string
        for char in s:
            print("-----")
            print("current = " + char)
            if char in close_open_relationships:
                # char is a closing bracket

                # make sure stack is not empty
                if not stack:
                    return False

                opening = stack.pop()
                # check if they are the same opening 
                if(close_open_relationships[char] == opening):
                    # valid closing open relationship
                    continue
                else:
                    return False
            else:
                # char is an opening bracket
                # push the opening bracket into the stacket
                stack.append(char)
            
            print("-----")

        # make sure is empty
        if stack:
            return False

        return True