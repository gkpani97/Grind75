# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # do an in order traversal
        def in_order_traversal(n):
            out = []
            if n.left:
                out += in_order_traversal(n.left)
            out += [n.val]
            if n.right:
                out += in_order_traversal(n.right)
            
            return out
        
        check_list = [-math.inf] + in_order_traversal(root) + [math.inf]
        
        # check if every element is smaller than the next element (and also if it is greater than previous, but this gets adjusted in the smaller than check.) Think more for realization.
        for i in range(1, len(check_list) - 1):
            if check_list[i] >= check_list[i + 1]:
                return False
        return True
