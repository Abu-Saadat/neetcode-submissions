# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hm = {val:idx for idx,val in enumerate(inorder)}
        preorderidx = [0]
        def arr_to_tree(l,r):
            if l>r: return None
            rootval = preorder[preorderidx[0]]
            preorderidx[0] +=1
            root = TreeNode(rootval)
            root.left = arr_to_tree(l,inorder_hm[rootval]-1)
            root.right = arr_to_tree(inorder_hm[rootval]+1,r)
            return root
        return arr_to_tree(0, len(preorder)-1)