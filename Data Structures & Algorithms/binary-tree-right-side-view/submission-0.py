# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            lenq = len(queue)
            rightside = None
            for i in range(lenq):
                node = queue.popleft()
                if node:
                    rightside = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightside:
                ans.append(rightside.val)
        return ans