# Definition for a binary tree node.
from typing import Optional
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root: 
            if subRoot :
                if root.val == subRoot.val:
                    return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
                else:
                    return False
            else:
                return False
        else:
            return False
        

if __name__ == "__main__":
    s = Solution()
    def build_tree(nodes):
        if not nodes:
            return None
        val = nodes.pop(0)
        if val is None:
            return None
        node = TreeNode(val)
        node.left = build_tree(nodes)
        node.right = build_tree(nodes)
        return node
    root = build_tree(config.C4_ARG[1])
    subRoot = build_tree(config.C4_ARG[2])
    
    for i in range(config.C4_ARG[0]):
        print(s.isSubtree(root, subRoot))