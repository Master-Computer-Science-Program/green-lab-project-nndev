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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    for i in range(int(config.C1_ARG[0])):
        node1 = TreeNode(int(config.C1_ARG[1]), TreeNode(int(config.C1_ARG[2])), TreeNode(config.C1_ARG[3]))
        node2 = TreeNode(int(config.C1_ARG[4]), TreeNode(int(config.C1_ARG[5])), TreeNode(int(config.C1_ARG[6])))
        print(s.isSameTree(node1, node2))