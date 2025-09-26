from typing import Optional
import sys

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
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    node1 = TreeNode(int(sys.argv[1]), TreeNode(int(sys.argv[2])), TreeNode(int(sys.argv[3])))
    node2 = TreeNode(int(sys.argv[4]), TreeNode(int(sys.argv[5])), TreeNode(int(sys.argv[6])))
    print(s.isSameTree(node1, node2))