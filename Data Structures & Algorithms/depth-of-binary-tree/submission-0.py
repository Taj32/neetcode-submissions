# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        current_depth = 0
        global_depth = 0

        if(root != None):
            print("current Node: " + str(root.val))
        
            if(root.left != None or root.right != None):
                #Branch left:
                left_depth = global_depth + self.maxDepth(root.left)

                #Branch right:
                right_depth = global_depth + self.maxDepth(root.right)
                
                # compare the left and right
                if(left_depth > right_depth):
                    global_depth = left_depth
                else:
                    global_depth = right_depth

            global_depth += 1
        return global_depth
        