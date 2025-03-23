# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        nodes1=[]
        nodes2=[]
        def traverse(root,nodes):
            if not root:
                nodes.append(None)
                return 
            nodes.append(root.val)
            traverse(root.left,nodes)
            traverse(root.right,nodes)
        traverse(p,nodes1)
        traverse(q,nodes2)
        return nodes1==nodes2
            