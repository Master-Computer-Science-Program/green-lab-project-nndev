import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
import time

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
if __name__ == "__main__":
    start = time.time()
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
    
    root = build_tree(config.C5_ARG[1])
    p = TreeNode(config.C5_ARG[2])
    q = TreeNode(config.C5_ARG[3])

    for i in range(config.C5_ARG[0]):
        print(s.lowestCommonAncestor(root, p, q).val)
    end = time.time()
    print("Elapsed time:", end - start, "seconds")