# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q=[]
        q.append(root)
        while q:
            lst=[]
            for i in range(len(q)):
                node=q.pop(0)
                lst.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lst)
        return res[::-1]