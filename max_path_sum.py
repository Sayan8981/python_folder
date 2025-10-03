"""
Module: max_path_sum
--------------------
Find the maximum path sum in a binary tree.
"""
from typing import Optional

class TreeNode:
    """Binary Tree Node structure."""
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"
    
class MaxPathSum:
    def __init__(self):
        self.max_sum = float('-inf') #represents negative infinity (−∞)
        #a special floating-point value that is smaller than any other number.
        
    def find_max_path_sum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:

            if not node:
                return 0
            
            left_gain = max(dfs(node.left),0)
            right_gain = max(dfs(node.right),0)
            
            current_path_sum = node.val + left_gain + right_gain
            
            self.max_sum = max(self.max_sum , current_path_sum)
            return node.val + max(left_gain, right_gain)
            
        dfs(root)
        return self.max_sum
        
        

# -------------------------------
# Example usage (for testing)
# -------------------------------
if __name__ == "__main__":
    # Construct binary tree
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(-25)
    root.right.right.left = TreeNode(3)
    root.right.right.right = TreeNode(4)
    
    solver = MaxPathSum()
    result = solver.find_max_path_sum(root)
    print (f"max current path sum: {result}")
    
    
#    Input Tree:
        #     10
        #    /  \
        #   2   10
        #  / \    \
        # 20  1    -25
        #           / \
        #          3   4